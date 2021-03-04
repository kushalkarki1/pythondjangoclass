# def welcome(name):
#     print(f"Welcome {name}")

# def bye(name):
#     print(f"Bye bye {name}")

# def greet_ram(xyz, name):
#     xyz(name)

# greet_ram(welcome, "Hari")
# greet_ram(bye, "Ram")

# def decorate_func(abc):
#     def wrapper():
#         print("Before function")
#         abc()
#         print("After function")
#     return wrapper

# @decorate_func
# def demo_func():
#     print("This is function")

# print(demo_func)
# demo_func()
# d = decorate_func(demo_func)
# d()

def smart_vision(func):
    def wrapper(a, b):
        if b == 0:
            return "could not divide by zero"
        else:
            return func(a, b)
    return wrapper

@smart_vision
def division(a, b):
    return a/b

print(division(10, 5))
print(division(10, 0))

def is_user_required(func):
    def wrapper():
        if user is loggedin:
            func()
        else:
            return "User is not logged in"



def product_list():
    pass

@is_user_required
def sales_report():
    pass

@is_user_required
def order_list():
    pass