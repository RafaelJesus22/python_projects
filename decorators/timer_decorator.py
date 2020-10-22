def timer_decorator(orig_func):
    def wrapper_function(*args, **kwargs):
        
        from time import time

        t1 = time()
        orig_func(*args, **kwargs)
        t2 = time()
        print(f"ran '{orig_func.__name__} in {t2 - t1} seconds'")

    return wrapper_function

@timer_decorator
def hello():
    print("Hello")


hello()