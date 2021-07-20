---
title: Caching
---

# Caching
- <span style="color:indianred">`lru_cache`</span>
- <span style="color:indianred">`cache`</span>
- <span style="color:indianred">`cached_property`</span>

--

## `lru_cache`

- <span style="color:indianred">`lru_cache(maxsize=128, typed=False)`</span>
- Wraps a function with a memoizing callable
- Saves time when an expensive function is sometimes called with the same arguments
- Caches results of _maxsize_ most recent calls
  - **LRU** stands for **L**east **R**ecently **U**sed
- If _typed_ is set to `True`, function arguments of different types will be cached separately

--

## `lru_cache` Attributes

- Function is also instrumented with 3 functions
  - <span style="color:indianred">`cache_info()`</span> - returns a named tuple showing _hits_, _misses_, _maxsize_ and _currsize_
  - <span style="color:indianred">`cache_clear()`</span> - clears/invalidates the cache
  - <span style="color:indianred">`cache_parameters()`</span> - new `dict` showing the values for _maxsize_ and _typed_

--

## Example: `lru_cache`

```python
{% include examples/04cache/fib.py %}
```
```python
>>> from fib import fib
>>> [fib(n) for n in range(16)]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
>>> fib.cache_info()
CacheInfo(hits=28, misses=16, maxsize=128, currsize=16)
>>> fib.cache_parameters()
{'maxsize': 128, 'typed': False}
```

--

## `lru_cache` Caveats

- Function's positional and keyword arguments must be hashable
  - Underlying storage is a dictionary
- Should only be used with pure functions
  - Same inputs always produce the same output
  - No side-effects

--

## `cache`

- Simple lightweight unbounded function cache
- Same as <span style="color:indianred">`lru_cache(maxsize=None)`</span>
- Because there is no eviction, it is smaller and faster than <span style="color:indianred">`lru_cache()`</span> with a size limit

--

## `cached_property`

- Similar to <span style="color:indianred">`property()`</span> with the addition of caching
- Value is computed once and then cached as a normal attribute for the life of the instance
- Unlike <span style="color:indianred">`property()`</span>, <span style="color:indianred">`cached_property`</span> allows writes without a setter being defined
- <span style="color:indianred">`cached_property`</span> only runs on lookup and only if the attribute does not already exist
- Once attribute exists, subsequent reads and writes work like a normal attribute

--

## Example: `cached_property`

```python
{% include examples/04cache/dataset.py %}
```
```python
>>> from random import random
>>> seq = (random() for _ in range(10_000_000))
>>> from dataset import DataSet
>>> d = DataSet(seq)
>>> import time
>>> time.time(), d.stdev, time.time()
(1626747711.129694, 0.28863495535352907, 1626747739.0964322)
>>> time.time(), d.stdev, time.time()
(1626747753.31688, 0.28863495535352907, 1626747753.3168828)
```