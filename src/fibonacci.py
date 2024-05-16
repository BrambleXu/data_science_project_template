import time


def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__}(args!r), kwargs!r)" f"-> {result!r}")
        return result

    return wrapper


@trace
def fibonacci(n):
    time.sleep(0.1)
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# use @trace decorator equal follows
# fibonacci = trace(fibonacci)
