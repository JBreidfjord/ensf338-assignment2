from timeit import timeit

import matplotlib.pyplot as plt

func_cache = {}


def func_original(n: int) -> int:
    if n == 0 or n == 1:
        return n

    return func_original(n - 1) + func_original(n - 2)


def func_cached(n: int) -> int:
    if n in func_cache:
        return func_cache[n]

    if n == 0 or n == 1:
        func_cache[n] = n
        return n

    result = func_cached(n - 1) + func_cached(n - 2)
    func_cache[n] = result
    return result


original_times = []
cached_times = []
for i in range(0, 36):
    func_cache = {}  # Reset cache

    original_time = timeit("func_original(i)", globals=globals(), number=1)
    original_times.append(original_time)

    cached_time = timeit("func_cached(i)", globals=globals(), number=1)
    cached_times.append(cached_time)

    print(f"n={i}, original={original_time}, cached={cached_time}")


plt.plot(original_times, label="original")
plt.plot(cached_times, label="cached")
plt.legend()
plt.xlabel("n")
plt.ylabel("time (s)")
plt.savefig("ex1.5.png")
