# loop
# [2, 4, 6, 8, 10]
# for i in <iterable_object>:
    # block of code
    # block of code

# alist = ["python", "PHP", "JS", "Java"]

# print(alist[0])
# print(alist[1])
# print(alist[2])
# print(alist[3])

# for i in alist:
#     print(i)

# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in a:
#     print(i)

# for i in range(100):
#     print(i)

# range(start, stop, step)
#range(100)
# start->0, stop->99, step->1

#range(2, 100)
# start->2, stop->99, step->1

#range(2, 100, 2)
# start->2, stop->99, step->2

# for i in range(2, 20, 2):
#     print(i)

# Take user input 10 times and print them
# alist = []
# for i in range(10):
#     n = input("enter anything: ")
#     alist.append(n)

# print(alist)

# create empty list
# take user input 10 times (convert to int)
# add all user input to that list
# print that list and
# sum of all numbers in that list

alist = []
total_sum = 0
for i in range(10):
    num = int(input("Enter any number: "))
    alist.append(num)
    print(f"Initial value: {total_sum}")
    total_sum = total_sum + num
    print(f"Final value: {total_sum}")

print(alist)
print(total_sum)