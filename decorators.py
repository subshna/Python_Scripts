'''
This example would show how the decorator works in a simple way
Refer the actual decorator symbol in decorators_2.py
'''
def new_decorator(original_func):

    def wrap_func():
        print ('Some code before the original function call')
        original_func()
        print ('Some code after the function')

    return wrap_func

def func_needs_decorator():
    print('This is to be decorated')

decorated_func = new_decorator(func_needs_decorator)
decorated_func()