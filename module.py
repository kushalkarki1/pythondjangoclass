sentence = "This is a sentence."
PI = 3.14

def area_of_circle(radius):
    return PI * radius * radius

def circumference_of_circle(radius):
    return 2 * PI * radius

if __name__ == "__main__":
    print(area_of_circle(7))
    print(circumference_of_circle(7))