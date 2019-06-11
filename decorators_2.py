def new_decorator(original_func):
    def wrap_func():
        print ('Some code before the original function')
        original_func()
        print ('Some code after the original function')

    return wrap_func

@new_decorator
def func_needs_decorator():
    print ('This wants decorators')

func_needs_decorator()