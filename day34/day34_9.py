def creator(a, b):
    print(f"Creation of decorators! with args {a}, {b}")

    def decorator(func):
        print(f"Decorator !!! with params {a}, {b}")

        def wrapped(x, y):
            print(f"I am wrapper with decorator params {a}, {b} and function {x}, {y} ")
            return func(x, y)

        return wrapped

    print("return decorator!")

    return decorator

@creator(2,3)
def function(x, y ):
    print(
        f"I am function!with  params {x}, {y}")


function(4,5)
