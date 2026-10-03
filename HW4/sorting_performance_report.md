# Sorting Algorithm Performance Benchmark

## Experimental setup

- List sizes tested: 10, 100, 1000, 10,000, and 50,000
- Each list was filled with random integers between 0 and 999,999.
- Each experiment was repeated 3 times for each algorithm and list size.
- Timing was measured using Python's `time.perf_counter()` function.
- Each timing run sorts a fresh copy of the generated data so all algorithms are tested on the same input.

## Runtime table (seconds)

| List size | Insertion sort | Heap sort | Quick sort | Radix sort |
|---:|---:|---:|---:|---:|
| 10 | 0.000012 | 0.000010 | 0.000025 | 0.000056 |
| 100 | 0.000227 | 0.000079 | 0.000111 | 0.000121 |
| 1000 | 0.030919 | 0.001512 | 0.002167 | 0.001292 |
| 10000 | 3.816122 | 0.031421 | 0.042105 | 0.016504 |
| 50000 | 89.413555 | 0.157853 | 0.184526 | 0.091720 |

## Observations

- Insertion sort is the slowest on larger lists because its running time grows quadratically with input size.
- Heap sort and quick sort are much faster on medium and large inputs, with runtimes growing roughly n log n.
- Radix sort is especially competitive for integer data because its runtime depends on digits rather than comparing values directly.
- For the random integer data used here, the fast comparison-based algorithms are usually best once the list is large enough, while insertion sort is only reasonable for very small arrays.

## Conclusion

For these experiments, the fastest method depends on the input size and data type. Radix sort performs very well on integer data and large arrays, while insertion sort becomes impractical quickly as n grows. Heap sort and quick sort are consistently strong general-purpose choices for larger lists.
