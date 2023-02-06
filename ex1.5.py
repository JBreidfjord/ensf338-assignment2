from functools import cache
from timeit import timeit

import matplotlib.pyplot as plt


def func_original(n: int) -> int:
    if n == 0 or n == 1:
        return n

    return func_original(n - 1) + func_original(n - 2)


@cache
def func_cached(n: int) -> int:
    if n == 0 or n == 1:
        return n

    return func_cached(n - 1) + func_cached(n - 2)


original_times = []
cached_times = []
iterations = 10
for i in range(0, 36):
    original_time = timeit("func_original(i)", globals=globals(), number=iterations) / iterations
    cached_time = timeit("func_cached(i)", globals=globals(), number=iterations) / iterations

    print(f"n={i}, original={original_time}, cached={cached_time}")

    original_times.append(original_time)
    cached_times.append(cached_time)

plt.plot(original_times, label="original")
plt.plot(cached_times, label="cached")
plt.legend()
plt.xlabel("n")
plt.ylabel("time (s)")
plt.savefig("ex1.5.png")
