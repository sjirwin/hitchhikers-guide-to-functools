---
title: Function Wrappers
---

# Function Wrappers
- <span style="color:indianred">`wraps`</span>
- <span style="color:indianred">`update_wrapper`</span>

--

## `wraps`

- <span style="color:indianred">`wraps(wrapped)`</span>
- A function decorator used when defining a wrapper function
- Updates the `wrapper` function attributes to be the same as the `wrapped` function
- Convenience decorator factory defined using <span style="color:indianred">`update_wrapper()`</span>

--

## Example: Without `wraps`

```python
>>> def my_decorator(f):
...     def wrapper(*args, **kwargs):
...         '''wrapper doc string'''
...         print('wrapper called')
...         return f(*args, **kwargs)
...     return wrapper
>>> @my_decorator
... def func():
...     '''func doc string'''
...     print('func called')
```
```python
>>> func()
wrapper called
func called
>>> func.__name__
'wrapper'
>>> func.__doc__
'wrapper doc string'
```

--

## Example: Using `wraps`

```python
>>> from functools import wraps
>>> def my_decorator_wraps(f):
...     @wraps(f)
...     def wrapper(*args, **kwargs):
...         '''wrapper doc string'''
...         print('wrapper called')
...         return f(*args, **kwargs)
...     return wrapper
>>> @my_decorator_wraps
... def func():
...     '''func doc string'''
...     print('func called')
```
```python
>>> func()
wrapper called
func called
>>> func.__name__
'func'
>>> func.__doc__
'func doc string'
```

--

## `update_wrapper`

- <span style="color:indianred">`update_wrapper(wrapper, wrapped)`</span>
- Rarely used directly
- Updates the `wrapper` function attributes to be the same as the `wrapped` function
- Useful in situations where <span style="color:indianred">`@wraps`</span> cannot be used
  - Wrapping a function after it is defined
  - Wrapping a function you do not own

--

## Example: `update_wrapper`

```python
>>> import string
>>> def my_capwords(s, sep=None):
...     '''my_capwords docstring'''
...     print('my_capwords')
...     return string.capwords(s, sep=sep)
>>> my_capwords('spam spam spam')
my_capwords
'Spam Spam Spam'
>>> my_capwords.__name__
'my_capwords'
```
```python
>>> from functools import update_wrapper
>>> capwords = update_wrapper(my_capwords, string.capwords)
>>> string.capwords.__name__, capwords.__name__, my_capwords.__name__
('capwords', 'capwords', 'capwords')
>>> capwords('spam spam spam')
my_capwords
'Spam Spam Spam'
```
