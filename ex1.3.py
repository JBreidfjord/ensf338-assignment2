# from functools import cache

# Can use custom cache, or alternatively use functools.cache
func_cache = {}

# @cache
def func(n):
    if n in func_cache:
        return func_cache[n]

    if n == 0 or n == 1:
        func_cache[n] = n
        return n

    result = func(n - 1) + func(n - 2)
    func_cache[n] = result
    return result
