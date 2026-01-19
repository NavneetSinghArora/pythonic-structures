# Pythonic Structures

A repository dedicated to exploring and implementing efficient, "Pythonic" data structures and algorithms, with a focus on performance benchmarking and modern development practices.

## 🚀 Getting Started

This project uses `uv` for dependency management and `Task` for automation.

### Prerequisites

- [uv](https://github.com/astral-sh/uv) (Extremely fast Python package installer and resolver)
- [Task](https://taskfile.dev/) (A task runner / simpler alternative to Make)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/NavneetSinghArora/pythonic-structures.git
   cd pythonic-structures
   ```

2. **Setup the environment:**
   ```bash
   uv sync
   ```

3. **Install pre-commit hooks:**
   ```bash
   uv run pre-commit install
   ```

## 🛠 Usage

We use `Taskfile` to manage common development tasks. You can run `task --list` to see all available commands.

### Development Tasks

| Command | Description |
|---------|-------------|
| `task tests` | Run all tests (including benchmarks) |
| `task tests-only` | Run unit tests only |
| `task benchmarks` | Run performance benchmarks |
| `task format` | Format and fix linting issues with Ruff |
| `task lint` | Check for linting issues |

### Manual Execution

If you prefer using `uv` directly:
- **Run tests:** `uv run pytest`
- **Format code:** `uv run ruff format .`

## 📂 Project Structure

- `sorting/`: Implementations of various sorting algorithms.
- `utils/`: Utility functions and decorators (e.g., performance timers).
- `tests/`: Unit tests for ensuring correctness.
- `benchmarks/`: Performance tests and result tracking.

<!-- BENCHMARK_START -->

## 📊 Benchmark Results

### System Information

- **CPU**: Apple M4
- **Architecture**: arm64
- **Python**: 3.14.2
- **OS**: Darwin 25.2.0

### Sorting Algorithms

| Algorithm | Mean | Min | Max | Std Dev | Ops/s | Rounds |
|-----------|------|-----|-----|---------|-------|--------|
| Native Sort | 260.90 ns | 228.05 ns | 3.66 µs | 32.68 ns | 3.83M ops/s | 195,123 |
| Bubble Sort | 15.89 µs | 15.04 µs | 682.25 µs | 7.17 µs | 62.93K ops/s | 9,026 |
| Insertion Sort | 52.67 µs | 49.33 µs | 503.79 µs | 6.88 µs | 18.99K ops/s | 13,023 |

<!-- BENCHMARK_END -->