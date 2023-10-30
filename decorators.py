# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()

def greet_decorator(func):
    def inner():
        print("Hi User!! Thanks for using this app.")
        func()
        print("Good night. Now sleep..")
    return inner

@greet_decorator
def say_hi():
    print("You said hi!!!")

say_hi()

