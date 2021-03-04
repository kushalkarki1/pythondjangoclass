# def outer_func():
#     print("I am outer")
#     def inner_func():
#         print("I am inner function")
#     return inner_func

# infunc = outer_func()
# infunc()
# infunc()
# infunc()
# infunc()


# def multiplier(n):
#     def multiply(a):
#         return a * n
#     return multiply

# times = multiplier(10)
# del multiplier
# print(times(5))
# print(times(3))

# a = 10
# def func():
#     global a
#     a = a + 1
#     print(f"Value of a: {a}")

# func()

# alist = [1, 2,]

# def func():
#     alist.append(5)
#     print(alist)

# func()

# def outer():
#     a = 10
#     def inner():
#         nonlocal a
#         a = a + 1
#         print(a)
#     inner()

# outer()

def greet(name):
    print(f"Welcome {name}")

def bye(name):
    print(f"Bye bye {name}")

def greet_ram(func):
    func("Ram")

greet_ram(greet)
greet_ram(bye)