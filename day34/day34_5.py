def p_decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        for a in args :
            print(a)
    return wrapper

@p_decorator
def myprint(*args):
    print(*args)
    
myprint("Listen", "tome")
    
