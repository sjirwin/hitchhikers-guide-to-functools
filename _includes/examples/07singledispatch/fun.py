from functools import singledispatch
@singledispatch
def fun(arg):
    print(f"Let me just say, {arg}")
@fun.register
def _(arg: int):
    print(f"Strength in numbers, eh? {arg}")
@fun.register
def _(arg: list):
    print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem)
@fun.register(complex)
def _(arg):
    print(f"Better than complicated. {arg.real} {arg.imag}")