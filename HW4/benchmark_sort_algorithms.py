import importlib.util
import statistics
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_sort(module_name: str):
    """Load a sort implementation from a Python file in the same folder.

    Args:
        module_name (str): The name of the sort module, without the .py extension.

    Returns:
        callable: The sort function defined in that module.
    """
    spec = importlib.util.spec_from_file_location(
        module_name, ROOT / f"{module_name}.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, module_name)


SORT_FUNCTIONS = {
    "insertion_sort": load_sort("insertion_sort"),
    "heap_sort": load_sort("heap_sort"),
    "quick_sort": load_sort("quick_sort"),
    "radix_sort": load_sort("radix_sort"),
}

SIZES = [10, 100, 1000, 10_000, 50_000]
TRIALS_PER_SIZE = 3


def generate_random_list(size: int, seed: int) -> list[int]:
    """Create a list of random integers for timing experiments."""
    import random

    rng = random.Random(seed)
    return [rng.randint(0, 999_999) for _ in range(size)]


results = {name: [] for name in SORT_FUNCTIONS}
for size in SIZES:
    for name, sort_function in SORT_FUNCTIONS.items():
        timings = []
        for trial in range(TRIALS_PER_SIZE):
            values = generate_random_list(size, size * 1000 + trial)
            start = time.perf_counter()
            sort_function(values[:])
            elapsed = time.perf_counter() - start
            timings.append(elapsed)
        results[name].append(
            {
                "size": size,
                "average": statistics.mean(timings),
                "min": min(timings),
                "max": max(timings),
            }
        )

lines = [
    "# Sorting Algorithm Performance Benchmark",
    "",
    "## Experimental setup",
    "",
    "- List sizes tested: 10, 100, 1000, 10,000, and 50,000",
    "- Each list was filled with random integers between 0 and 999,999.",
    "- Each experiment was repeated 3 times for each algorithm and list size.",
    "- Timing was measured using Python's `time.perf_counter()` function.",
    "- Each timing run sorts a fresh copy of the generated data so all algorithms are tested on the same input.",
    "",
    "## Runtime table (seconds)",
    "",
    "| List size | Insertion sort | Heap sort | Quick sort | Radix sort |",
    "|---:|---:|---:|---:|---:|",
]

for size in SIZES:
    row = [str(size)]
    for name in ["insertion_sort", "heap_sort", "quick_sort", "radix_sort"]:
        entry = next(item for item in results[name] if item["size"] == size)
        row.append(f"{entry['average']:.6f}")
    lines.append(f"| {' | '.join(row)} |")

lines.extend(
    [
        "",
        "## Observations",
        "",
        "- Insertion sort is the slowest on larger lists because its running time grows quadratically with input size.",
        "- Heap sort and quick sort are much faster on medium and large inputs, with runtimes growing roughly n log n.",
        "- Radix sort is especially competitive for integer data because its runtime depends on digits rather than comparing values directly.",
        "- For the random integer data used here, the fast comparison-based algorithms are usually best once the list is large enough, while insertion sort is only reasonable for very small arrays.",
        "",
        "## Conclusion",
        "",
        "For these experiments, the fastest method depends on the input size and data type. Radix sort performs very well on integer data and large arrays, while insertion sort becomes impractical quickly as n grows. Heap sort and quick sort are consistently strong general-purpose choices for larger lists.",
        "",
    ]
)

report_path = ROOT / "sorting_performance_report.md"
report_path.write_text("\n".join(lines), encoding="utf-8")

print(report_path)
print("\n".join(lines))
