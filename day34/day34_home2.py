from datetime import datetime

def logger(filename):
    def decor(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                with open(filename,"a") as file:
                    file.write(f"{func.__name__} {datetime.now()} : {result}\n")
            except Exception as ex:
                print(str(ex))
            return result
        return wrapper
    return decor
