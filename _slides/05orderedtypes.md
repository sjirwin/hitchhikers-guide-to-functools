---
title: Ordered Types
---

# Ordered Types
- <span style="color:indianred">`total_ordering`</span>

--

## `total_ordering`

- Class decorator that makes it easy to create well behaved totally ordered types
- If class defines at least one rich comparison operator, it supplies the rest
  - Class must define one of <span style="color:indianred">`__lt__()`</span>, <span style="color:indianred">`__le__()`</span>, <span style="color:indianred">`__gt__()`</span>, or <span style="color:indianred">`__ge__()`</span>
  - Additionally, class should supply an <span style="color:indianred">`__eq__()`</span> method
- **Caveat:** does come at the cost of slower execution and more complex stack traces for the derived comparison methods

--

## Example: `total_ordering`

```python
{% include examples/05orderedtypes/car.py %}
```
```python
>>> from car import Car
>>> car_1 = Car(2020, 'BMW', '530i')
>>> car_2 = Car(2020, 'BMW', '330i')
>>> (car_1 < car_2), (car_1 > car_2)
(False, True)
```
