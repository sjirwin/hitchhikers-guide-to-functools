---
title: Reduce
---

# Reduce
- <span style="color:indianred">`reduce`</span>

--

## `reduce`

- <span style="color:indianred">`reduce(function, iterable[, initializer])`</span>
- Applies _function_ of 2 arguments cumulatively to the items of _iterable_ to reduce it to a single value
  - Built-in function <span style="color:indianred">sum()</span> is an example of a reducer
- Example:
```python
>>> from functools import reduce
>>> import operator
>>> def product(iterable):
...     return reduce(operator.mul, iterable, 1)
>>> product([2,5,8])
80
>>> product(range(2,5))
24
```