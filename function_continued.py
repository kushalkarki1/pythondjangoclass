# def some_func(a, *args):
#     print(a)
#     print(args)

# some_func(1, 2, 3, 4, 5, 6, 7, 8)


def some_func(*args, **kwargs):
    print(args)
    print(kwargs)

some_func("python", "java", name="Binod", nickname="binod1")