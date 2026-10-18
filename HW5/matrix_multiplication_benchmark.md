# Matrix Multiplication Performance Benchmark

## Experimental setup

- Matrix sizes tested: 2, 4, 8, 16, 32, 64, 128, and 1000
- Each input matrix contains deterministic random integers from -10 to 9.
- For sizes 2 through 128, each method was timed 3 times per size. At size
  1000, each method was timed once in a separate run.
- Both methods used the same input matrices for each size.
- Correctness was checked before timing; the benchmark stops if results differ.
- For sizes 2 through 128, one untimed call to each method was made before
  collecting timings. The separate 1000 x 1000 run did not use a warm-up call.
- Timing used Python's `time.perf_counter()` function.
- Median time is used to compare methods; average, minimum, and maximum are also reported.
- Python version: 3.13.3
- Platform: Windows-11-10.0.22621-SP0

## Runtime table (seconds)

| Matrix size | Regular average | Regular median | Strassen average | Strassen median | Faster by median |
|---:|---:|---:|---:|---:|:---|
| 2 x 2 | 0.000010 | 0.000009 | 0.000010 | 0.000010 | Regular |
| 4 x 4 | 0.000041 | 0.000041 | 0.000098 | 0.000096 | Regular |
| 8 x 8 | 0.000517 | 0.000523 | 0.001056 | 0.001229 | Regular |
| 16 x 16 | 0.003372 | 0.003852 | 0.008031 | 0.008450 | Regular |
| 32 x 32 | 0.017253 | 0.016856 | 0.037939 | 0.037979 | Regular |
| 64 x 64 | 0.151866 | 0.151267 | 0.267867 | 0.269258 | Regular |
| 128 x 128 | 1.428919 | 1.427492 | 2.294034 | 2.242656 | Regular |
| 1000 x 1000 | 762.197000 | 762.197000 | 434.321000 | 434.321000 | Strassen |

## Crossover estimate

Strassen was not faster by median time in the repeated trials through
128 x 128. The single run at 1000 x 1000 was faster with Strassen, but more
repeated measurements are needed to establish a reliable crossover point. Not 
every measurement was run due to time and power constraints.

## Timing details

| Matrix size | Method | Minimum | Maximum |
|---:|:---|---:|---:|
| 2 x 2 | Regular | 0.000008 | 0.000014 |
| 2 x 2 | Strassen | 0.000008 | 0.000011 |
| 4 x 4 | Regular | 0.000040 | 0.000041 |
| 4 x 4 | Strassen | 0.000094 | 0.000103 |
| 8 x 8 | Regular | 0.000493 | 0.000536 |
| 8 x 8 | Strassen | 0.000703 | 0.001236 |
| 16 x 16 | Regular | 0.002398 | 0.003866 |
| 16 x 16 | Strassen | 0.006193 | 0.009451 |
| 32 x 32 | Regular | 0.016541 | 0.018362 |
| 32 x 32 | Strassen | 0.035006 | 0.040833 |
| 64 x 64 | Regular | 0.149971 | 0.154359 |
| 64 x 64 | Strassen | 0.258157 | 0.276186 |
| 128 x 128 | Regular | 1.397172 | 1.462093 |
| 128 x 128 | Strassen | 2.239331 | 2.400114 |
| 1000 x 1000 | Regular | 762.197000 | 762.197000 |
| 1000 x 1000 | Strassen | 434.321000 | 434.321000 |
