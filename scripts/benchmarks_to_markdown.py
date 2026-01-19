#!/usr/bin/env python3
"""Convert pytest-benchmark results.json to markdown and update README.md files.

Usage:
    python scripts/benchmarks_to_markdown.py

This script reads benchmarks/results.json, generates markdown tables with
benchmark results, and updates README files based on group markers.

Group markers in README files:
    <!-- Sorting Benchmarks will be added here group=sorting-->

The script looks for patterns like 'group=GROUPNAME' in comments and updates
the corresponding section with benchmarks from that group.
"""

import json
import re
import sys
from pathlib import Path


def format_time(seconds: float) -> str:
    """Format time in human-readable format with appropriate units."""
    if seconds < 1e-6:
        return f"{seconds * 1e9:.2f} ns"
    elif seconds < 1e-3:
        return f"{seconds * 1e6:.2f} µs"
    elif seconds < 1:
        return f"{seconds * 1e3:.2f} ms"
    else:
        return f"{seconds:.2f} s"


def format_ops(ops: float) -> str:
    """Format operations per second in human-readable format."""
    if ops >= 1e6:
        return f"{ops / 1e6:.2f}M ops/s"
    elif ops >= 1e3:
        return f"{ops / 1e3:.2f}K ops/s"
    else:
        return f"{ops:.2f} ops/s"


def generate_group_markdown(benchmarks: list, group_name: str) -> str:
    """Generate markdown content for a specific group of benchmarks."""
    lines = []

    # Table header
    lines.append(f"### 📊 {group_name.title()} Benchmarks\n")
    lines.append("| Algorithm | Mean | Min | Max | Std Dev | Ops/s | Rounds |")
    lines.append("|-----------|------|-----|-----|---------|-------|--------|")

    # Sort by mean time (fastest first)
    benchmarks.sort(key=lambda x: x.get("stats", {}).get("mean", float("inf")))

    for benchmark in benchmarks:
        name = benchmark.get("name", "Unknown")
        # Clean up the test name (remove test_benchmark_ prefix)
        display_name = name.replace("test_benchmark_", "").replace("_", " ").title()

        stats = benchmark.get("stats", {})
        mean = format_time(stats.get("mean", 0))
        min_time = format_time(stats.get("min", 0))
        max_time = format_time(stats.get("max", 0))
        stddev = format_time(stats.get("stddev", 0))
        ops = format_ops(stats.get("ops", 0))
        rounds = stats.get("rounds", 0)

        lines.append(f"| {display_name} | {mean} | {min_time} | {max_time} | {stddev} | {ops} | {rounds:,} |")

    return "\n".join(lines)


def generate_full_markdown(data: dict) -> str:
    """Generate full markdown content with system info and all benchmarks."""
    lines = []

    # Add header section
    lines.append("## 📊 Benchmark Results\n")

    # Add machine info
    machine = data.get("machine_info", {})
    cpu = machine.get("cpu", {})

    lines.append("### System Information\n")
    lines.append(f"- **CPU**: {cpu.get('brand_raw', 'Unknown')}")
    lines.append(f"- **Architecture**: {machine.get('machine', 'Unknown')}")
    lines.append(f"- **Python**: {machine.get('python_version', 'Unknown')}")
    lines.append(f"- **OS**: {machine.get('system', 'Unknown')} {machine.get('release', '')}\n")

    # Group benchmarks by group
    benchmarks = data.get("benchmarks", [])
    grouped: dict[str, list] = {}

    for benchmark in benchmarks:
        group = benchmark.get("group", "ungrouped")
        if group not in grouped:
            grouped[group] = []
        grouped[group].append(benchmark)

    # Generate tables for each group
    for group_name, group_benchmarks in grouped.items():
        lines.append(f"### {group_name.title()} Algorithms\n")

        # Table header
        lines.append("| Algorithm | Mean | Min | Max | Std Dev | Ops/s | Rounds |")
        lines.append("|-----------|------|-----|-----|---------|-------|--------|")

        # Sort by mean time (fastest first)
        group_benchmarks.sort(key=lambda x: x.get("stats", {}).get("mean", float("inf")))

        for benchmark in group_benchmarks:
            name = benchmark.get("name", "Unknown")
            display_name = name.replace("test_benchmark_", "").replace("_", " ").title()

            stats = benchmark.get("stats", {})
            mean = format_time(stats.get("mean", 0))
            min_time = format_time(stats.get("min", 0))
            max_time = format_time(stats.get("max", 0))
            stddev = format_time(stats.get("stddev", 0))
            ops = format_ops(stats.get("ops", 0))
            rounds = stats.get("rounds", 0)

            lines.append(f"| {display_name} | {mean} | {min_time} | {max_time} | {stddev} | {ops} | {rounds:,} |")

        lines.append("")

    return "\n".join(lines)


def find_and_update_group_readmes(project_root: Path, grouped_benchmarks: dict[str, list]) -> list[str]:
    """Find README files with group markers and update them."""
    updated_files = []

    # Pattern to match group markers like: <!-- ... group=sorting -->
    group_pattern = re.compile(r"<!--.*?group=(\w+).*?-->")

    # Find all README.md files in the project
    for readme_path in project_root.rglob("README.md"):
        content = readme_path.read_text()

        # Find all group markers in this file
        for match in group_pattern.finditer(content):
            group_name = match.group(1)

            if group_name in grouped_benchmarks:
                # Generate markdown for this group
                markdown = generate_group_markdown(grouped_benchmarks[group_name], group_name)

                # Define markers for this group
                start_marker = f"<!-- BENCHMARK_{group_name.upper()}_START -->"
                end_marker = f"<!-- BENCHMARK_{group_name.upper()}_END -->"

                # Check if markers already exist
                if start_marker in content and end_marker in content:
                    # Replace content between markers
                    start_idx = content.find(start_marker) + len(start_marker)
                    end_idx = content.find(end_marker)
                    new_content = content[:start_idx] + "\n\n" + markdown + "\n\n" + content[end_idx:]
                else:
                    # Replace the original group marker with markers and content
                    original_marker = match.group(0)
                    new_content = content.replace(original_marker, f"{start_marker}\n\n{markdown}\n\n{end_marker}")

                readme_path.write_text(new_content)
                updated_files.append(str(readme_path))
                content = new_content  # Update content for subsequent matches

    return updated_files


def update_main_readme(readme_path: Path, markdown_content: str) -> None:
    """Update the main README.md with full benchmark results."""
    start_marker = "<!-- BENCHMARK_START -->"
    end_marker = "<!-- BENCHMARK_END -->"

    content = readme_path.read_text()

    if start_marker in content and end_marker in content:
        start_idx = content.find(start_marker) + len(start_marker)
        end_idx = content.find(end_marker)
        new_content = content[:start_idx] + "\n\n" + markdown_content + "\n" + content[end_idx:]
    else:
        if "<!-- Benchmarks will be added here -->" in content:
            new_content = content.replace(
                "<!-- Benchmarks will be added here -->", f"{start_marker}\n\n{markdown_content}\n{end_marker}",
            )
        else:
            new_content = content.rstrip() + f"\n\n{start_marker}\n\n{markdown_content}\n{end_marker}\n"

    readme_path.write_text(new_content)


def main() -> int:
    """Main entry point."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    results_path = project_root / "benchmarks" / "results.json"
    main_readme_path = project_root / "README.md"

    if not results_path.exists():
        print(f"Error: Results file not found: {results_path}", file=sys.stderr)
        return 1

    # Load benchmark results
    try:
        with results_path.open() as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON: {e}", file=sys.stderr)
        return 1

    # Group benchmarks by group
    benchmarks = data.get("benchmarks", [])
    grouped: dict[str, list] = {}

    for benchmark in benchmarks:
        group = benchmark.get("group", "ungrouped")
        if group not in grouped:
            grouped[group] = []
        grouped[group].append(benchmark)

    # Update group-specific README files
    updated_files = find_and_update_group_readmes(project_root, grouped)

    for file in updated_files:
        print(f"✅ Updated group-specific README: {file}")

    # Update main README with full results
    if main_readme_path.exists():
        full_markdown = generate_full_markdown(data)
        update_main_readme(main_readme_path, full_markdown)
        print(f"✅ Updated main README: {main_readme_path}")

    if not updated_files:
        print("ℹ️  No group-specific README files found with group markers.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
