# Decorator Function
def log_decorator(func):
    def wrapper():
        print("Function is being called...")
        func()
        print("Function finished.")
    return wrapper

# Decorated Function
@log_decorator
def say_hello():
    print("Hello!")

# Call the Function
say_hello()
