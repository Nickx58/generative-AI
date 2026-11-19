def my_decorator(func):
    def wrapper():
        print("Before Function Runs")
        func()
        print("After Function Runs")
    return wrapper

@my_decorator
def greet():
    print("Hello from Deco")

greet()