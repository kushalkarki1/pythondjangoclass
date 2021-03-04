# Loop (Iteration)

# Types:
    # 1. Bounded Loop - for
    # 2. Unbounded Loop - while

# while <condition>:
    # block of codes
    # block of codes

# choice = "y"
# while choice == "y":
#     num1 = int(input("Enter any number: "))
#     num2 = int(input("Enter another number: "))
#     print(f"Sum of {num1} and {num2} is {num1+num2}.")
#     choice = input("do you want to continue (y/n)?")

# ask user for password until user input "abcde"
# if password is correct, print successful.

# password = input("Enter your password: ")
# while password != "abcde":
#     password = input("Enter your password: ")

# print("successful")

# break
# continue

# for i in range(1, 10):
#     print(f"Before break: {i}")
#     if i % 2 == 0:
#         break
#     print(f"After break: {i}")

# print("-"*10)

# for i in range(1, 10):
#     print(f"Before continue: {i}")
#     if i % 2 == 0:
#         continue
#     print(f"After continue: {i}")

# for
# else

for i in range(1, 10):
    if i % 3 == 0:
        break
    print(i)
else:
    print("Loop completed")

# while
# else