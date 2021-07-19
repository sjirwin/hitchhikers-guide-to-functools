from functools import partial
pow_2 = partial(pow, exp=2)
print(f'{pow_2(5)=}') # pow_2(5)=25