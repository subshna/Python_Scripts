Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
================== RESTART: C:/Users/srisani/Desktop/mod.py ==================
10
>>> 
================== RESTART: C:/Users/srisani/Desktop/mod.py ==================

Traceback (most recent call last):
  File "C:/Users/srisani/Desktop/mod.py", line 3, in <module>
    print x/0
ZeroDivisionError: integer division or modulo by zero
>>> 
================== RESTART: C:/Users/srisani/Desktop/mod.py ==================
46691876 46691756 46691876
>>> 
================== RESTART: C:/Users/srisani/Desktop/mod.py ==================
46757412 46757412 46757412
>>> 
================== RESTART: C:/Users/srisani/Desktop/mod.py ==================
51980240 51980240 51980240
>>> locals()
{'a': 2000, 'c': 2000, 'b': 2000, '__builtins__': <module '__builtin__' (built-in)>, '__file__': 'C:/Users/srisani/Desktop/mod.py', '__package__': None, '__name__': '__main__', '__doc__': None}
>>> d=2000
>>> id(d)
51980288
>>> #What if i assign a value say a= "Test" and b= 200 after  values a=10 and b=20 ? Does this give error as i changed the datatype of 'a' variable ?
>>> a="Test"
>>> type(a)
<type 'str'>
>>> a=10
>>> type(a)
<type 'int'>
>>> a=2**32
>>> a
4294967296L
>>> type(a)
<type 'long'>
>>> a=4294967295
>>> type(a)
<type 'long'>
>>> a=2**31
>>> a
2147483648L
>>> type(a)
<type 'long'>
>>> a=2147483647
>>> type(a)
<type 'int'>
>>> type("10")
<type 'str'>
>>> int("10")
10
>>> str(10)
'10'
>>> # interactive mode of operation, script mode
>>> def f():
	pass

>>> class A:
	pass

>>> locals()
{'a': 2147483647, 'A': <class __main__.A at 0x027CFBC8>, 'c': 2000, 'b': 2000, 'd': 2000, 'f': <function f at 0x031BEC30>, '__builtins__': <module '__builtin__' (built-in)>, '__file__': 'C:/Users/srisani/Desktop/mod.py', '__package__': None, '__name__': '__main__', '__doc__': None}
>>> a
2147483647
>>> b
2000
>>> c
2000
>>> 
================== RESTART: C:/Users/srisani/Desktop/def.py ==================
10 10000000000 1.0 (1+10j) [1, 2, 3, 4]
Function f
>>> import def
SyntaxError: invalid syntax
>>> import deff
10 10000000000 1.0 (1+10j) [1, 2, 3, 4]
Function f
>>> 1+2j
(1+2j)
>>> 1000
1000
>>> "Wipro"
'Wipro'
>>> a=10
>>> type(a)
<type 'int'>
>>> a=100000000000
>>> type(a)
<type 'long'>
>>> def a():
	pass

>>> type(a)
<type 'function'>
>>> a=10
>>> A=100
>>> a
10
>>> A
100
>>> help("keywords")

Here is a list of the Python keywords.  Enter any keyword to get more help.

and                 elif                if                  print
as                  else                import              raise
assert              except              in                  return
break               exec                is                  try
class               finally             lambda              while
continue            for                 not                 with
def                 from                or                  yield
del                 global              pass                

>>> import math
>>> math.pi
3.141592653589793
>>> math.e
2.718281828459045
>>> math.pi=100
>>> math.pi
100
>>> a=10
>>> type(a)
<type 'int'>
>>> a=10.0
>>> type(a)
<type 'float'>
>>> a=10**10
>>> a
10000000000L
>>> a=10+1j
>>> b=10-1j
>>> a
(10+1j)
>>> type(a)
<type 'complex'>
>>> type(b)
<type 'complex'>
>>> a*b
(101+0j)
>>> a=10
>>> #__repr__, __str__
>>> dir(10)
['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__float__', '__floordiv__', '__format__', '__getattribute__', '__getnewargs__', '__hash__', '__hex__', '__index__', '__init__', '__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__', '__new__', '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']
>>> 10+20
30
>>> (10).__add__(20)
30
>>> help("keywords")

Here is a list of the Python keywords.  Enter any keyword to get more help.

and                 elif                if                  print
as                  else                import              raise
assert              except              in                  return
break               exec                is                  try
class               finally             lambda              while
continue            for                 not                 with
def                 from                or                  yield
del                 global              pass                

>>> 
