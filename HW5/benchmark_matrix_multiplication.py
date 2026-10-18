import platform
import statistics
import sys
import time
from pathlib import Path
from typing import Callable

import numpy as np

from matrix import Matrix


ROOT = Path(__file__).resolve().parent
SIZES = [2, 4, 8, 16, 32, 64, 128]
TRIALS_PER_SIZE = 3
RANDOM_VALUE_LIMIT = 10


def generate_matrices(size: int, seed: int) -> tuple[Matrix, Matrix]:
    """Create a repeatable pair of square matrices for benchmarking.

    Args:
        size (int): The number of rows and columns in each matrix.
        seed (int): The seed used to generate matrix values.

    Returns:
        tuple[Matrix, Matrix]: The generated left and right matrices.
    """
    rng = np.random.default_rng(seed)
    left = Matrix(size)
    right = Matrix(size)
    left.matrix[:, :] = rng.integers(
        -RANDOM_VALUE_LIMIT, RANDOM_VALUE_LIMIT, size=(size, size)
    )
    right.matrix[:, :] = rng.integers(
        -RANDOM_VALUE_LIMIT, RANDOM_VALUE_LIMIT, size=(size, size)
    )
    return left, right


def time_multiplication(
    multiply_function: Callable[[Matrix], Matrix],
    matrix: Matrix,
) -> float:
    """Time one multiplication call in seconds."""
    start = time.perf_counter()
    multiply_function(matrix)
    return time.perf_counter() - start


results = []
for size in SIZES:
    left, right = generate_matrices(size, seed=size)

    regular_result = left.multiply(right)
    strassen_result = left.strassenMultiply(right)
    if not np.array_equal(regular_result.matrix, strassen_result.matrix):
        raise AssertionError(f"Multiplication results differ for size {size}.")

    # Run each implementation once before timing to reduce startup effects.
    left.multiply(right)
    left.strassenMultiply(right)

    regular_timings = []
    strassen_timings = []
    for trial in range(TRIALS_PER_SIZE):
        if trial % 2 == 0:
            regular_timings.append(time_multiplication(left.multiply, right))
            strassen_timings.append(
                time_multiplication(left.strassenMultiply, right)
            )
        else:
            strassen_timings.append(
                time_multiplication(left.strassenMultiply, right)
            )
            regular_timings.append(time_multiplication(left.multiply, right))

    results.append(
        {
            "size": size,
            "regular": {
                "average": statistics.mean(regular_timings),
                "median": statistics.median(regular_timings),
                "min": min(regular_timings),
                "max": max(regular_timings),
            },
            "strassen": {
                "average": statistics.mean(strassen_timings),
                "median": statistics.median(strassen_timings),
                "min": min(strassen_timings),
                "max": max(strassen_timings),
            },
        }
    )


faster_sizes = [
    result["size"]
    for result in results
    if result["strassen"]["median"] < result["regular"]["median"]
]
if faster_sizes:
    crossover = (
        f"The first tested size where Strassen was faster by median time was "
        f"{faster_sizes[0]} x {faster_sizes[0]}."
    )
else:
    crossover = (
        "Strassen was not faster by median time at any tested size; "
        "no crossover was observed."
    )

lines = [
    "# Matrix Multiplication Performance Benchmark",
    "",
    "## Experimental setup",
    "",
    f"- Matrix sizes tested: {', '.join(map(str, SIZES))}",
    f"- Each input matrix contains deterministic random integers from "
    f"{-RANDOM_VALUE_LIMIT} to {RANDOM_VALUE_LIMIT - 1}.",
    f"- Each method was timed {TRIALS_PER_SIZE} times per size.",
    "- Both methods used the same input matrices for each size.",
    "- Correctness was checked before timing; the benchmark stops if results differ.",
    "- One untimed call to each method was made before collecting timings.",
    "- Timing used Python's `time.perf_counter()` function.",
    "- Median time is used to compare methods; average, minimum, and maximum "
    "are also reported.",
    f"- Python version: {sys.version.split()[0]}",
    f"- Platform: {platform.platform()}",
    "",
    "## Runtime table (seconds)",
    "",
    "| Matrix size | Regular average | Regular median | Strassen average | "
    "Strassen median | Faster by median |",
    "|---:|---:|---:|---:|---:|:---|",
]

for result in results:
    size = result["size"]
    regular = result["regular"]
    strassen = result["strassen"]
    faster = "Strassen" if strassen["median"] < regular["median"] else "Regular"
    lines.append(
        f"| {size} x {size} | {regular['average']:.6f} | "
        f"{regular['median']:.6f} | {strassen['average']:.6f} | "
        f"{strassen['median']:.6f} | {faster} |"
    )

lines.extend(
    [
        "",
        "## Crossover estimate",
        "",
        crossover,
        "",
        "This is an empirical estimate for this machine, Python version, and "
        "implementation. Use the measurements to choose a hybrid cutoff, and "
        "rerun the benchmark on the machine where the code will be used.",
        "",
        "## Timing details",
        "",
        "| Matrix size | Method | Minimum | Maximum |",
        "|---:|:---|---:|---:|",
    ]
)

for result in results:
    size = result["size"]
    for method, label in (("regular", "Regular"), ("strassen", "Strassen")):
        timings = result[method]
        lines.append(
            f"| {size} x {size} | {label} | {timings['min']:.6f} | "
            f"{timings['max']:.6f} |"
        )

lines.append("")

report_path = ROOT / "matrix_multiplication_benchmark.md"
report_path.write_text("\n".join(lines), encoding="utf-8")

print(report_path)
print("\n".join(lines))
