import math

# Taking the input from user
number = int(input("Enter the Number"))

root = math.sqrt(number)
if int(root) ** 2 == number:
    print(number, "is a perfect square")
else:
    print(number, "is not a perfect square")

def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1

print(find_next_square(25))
