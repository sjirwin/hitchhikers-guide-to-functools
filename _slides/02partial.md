---
title: Simplifying function signatures
---

# Simplifying Function Signatures

--

## `partial`

- Takes as input a function and the arguments to "lock in"
- Returns a <span style="color:indianred">`partial object`</span> which behaves like the original function called with those arguments already defined

```python
{% include examples/02partial/pow2.py %}
```

--

## Reduce Arguments

- Use <span style="color:indianred">`partial`</span> to transform a multi-argument function to a single argument function in places where that is required (e.g., <span style="color:indianred">`map`</span>)
- Possible without <span style="color:indianred">`partial`</span>, but is more verbose

```python
>>> from functools import partial
>>> list(map(partial(pow, exp=3), range(10)))
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
```

```python
>>> def pow_3(x):
...     return pow(x, 3)
>>> list(map(pow_3, range(10)))
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

>>> list(map(lambda x: pow(x, 3), range(10)))
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
```

--

## Simplify Code

- Define functions that are easier to type, read, and friendly to code completion

```python
{% include examples/02partial/printerror.py %}
```

--

## `partialmethod`

- Easiest to think of it as <span style="color:indianred">`partial`</span> for methods
- From the Python [docs](https://docs.python.org/3/library/functools.html#functools.partialmethod)
> Returns a new <span style="color:indianred">`partialmethod`</span> descriptor which behaves like <span style="color:indianred">`partial`</span> except that it is designed to be used as a method definition rather than being directly callable.
- The function argument must be a descriptor or a callable

--

## Example

```python
{% include examples/02partial/cell.py %}
```
```python
>>> from cell import Cell
>>> c = Cell()
>>> c.alive
False
>>> c.set_alive()
>>> c.alive
True
```
