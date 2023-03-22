def creator():
    print("Creation of decorators!")
    
    def decorator(func):
        print("Decorator !!!")
        
        def wrapped():
            print("I am wrapper")
            return func()
        
        return wrapped()

    print("return decorator!")
    
    return decorator

def function():
    print("I am function!")
    
new_decor = creator()

decorated_function = new_decor(function)
