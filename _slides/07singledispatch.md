---
title: Function Overloading
---

# Function Overloading
- <span style="color:indianred">`singledispatch`</span>
- <span style="color:indianred">`singledispatchmethod`</span>

--

## `singledispatch`

- Function decorator which transforms a function into a single-dispatch generic function
  - Means implementation is chosen based on the type of a single argument
- Generic function is decorated with <span style="color:indianred">`@singledispatch`</span>
- Overloaded implementations are decorated with the <span style="color:indianred">`register()`</span> attribute of the generic function
  - If implementation is annotated with types, the decorator will automatically infer the type of the argument
  - Otherwise, the type is an argument to the decorator

--

## Example: `singledispatch`

```python
{% include examples/07singledispatch/fun.py %}
```

--

## Example: `singledispatch`

```python
>>> from fun import fun
>>> fun(9)
Strength in numbers, eh? 9
>>> fun([9,7])
Enumerate this:
0 9
1 7
>>> fun(3.4)
Let me just say, 3.4
>>> fun(3.4 + 6j)
Better than complicated. 3.4 6.0
```

--

## `singledispatchmethod`

- Single dispatch for methods
- Function decorator which transforms a method into a single-dispatch generic function
  - Dispatch happens on the type of the first non-`self` or non-`cls` argument