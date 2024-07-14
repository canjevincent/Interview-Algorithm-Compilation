#1. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

# Import the math module to access mathematical functions like pi
import math

# Define a class called Circle to represent a circle
class Circle:
    # Initialize the Circle object with a given radius
    def __init__(self, radius):
        self.radius = radius
    
    # Calculate and return the area of the circle using the formula: π * r^2
    def calculate_circle_area(self):
        return math.pi * self.radius**2
    
    # Calculate and return the perimeter (circumference) of the circle using the formula: 2π * r
    def calculate_circle_perimeter(self):
        return 2 * math.pi * self.radius

# Example usage
# Prompt the user to input the radius of the circle and convert it to a floating-point number
radius = float(input("Input the radius of the circle: "))

# Create a Circle object with the provided radius
circle = Circle(radius)

# Calculate the area of the circle using the calculate_circle_area method
area = circle.calculate_circle_area()

# Calculate the perimeter of the circle using the calculate_circle_perimeter method
perimeter = circle.calculate_circle_perimeter()

# Display the calculated area and perimeter of the circle
print("Area of the circle:", area)
print("Perimeter of the circle:", perimeter) 

#2. Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.

# Import the date class from the datetime module to work with dates
from datetime import date

# Define a class called Person to represent a person with a name, country, and date of birth
class Person:
    # Initialize the Person object with a name, country, and date of birth
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
    
    # Calculate the age of the person based on their date of birth
    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

# Example usage
# Create three Person objects with different attributes
person1 = Person("Ferdi Odilia", "France", date(1962, 7, 12))
person2 = Person("Shweta Maddox", "Canada", date(1982, 10, 20))
person3 = Person("Elizaveta Tilman", "USA", date(2000, 1, 1))

# Access and print the attributes and calculated age for each person
print("Person 1:")
print("Name:", person1.name)
print("Country:", person1.country)
print("Date of Birth:", person1.date_of birth)
print("Age:", person1.calculate_age())

print("\nPerson 2:")
print("Name:", person2.name)
print("Country:", person2.country)
print("Date of Birth:", person2.date_of birth)
print("Age:", person2.calculate_age())

print("\nPerson 3:")
print("Name:", person3.name)
print("Country:", person3.country)
print("Date of Birth:", person3.date_of birth)
print("Age:", person3.calculate_age())

#3. Write a Python program to create a calculator class. Include methods for basic arithmetic operations.

# Define a class called Calculator to perform basic arithmetic operations
class Calculator:
    # Define a method for addition that takes two arguments and returns their sum
    def add(self, x, y):
        return x + y

    # Define a method for subtraction that takes two arguments and returns their difference
    def subtract(self, x, y):
        return x - y

    # Define a method for multiplication that takes two arguments and returns their product
    def multiply(self, x, y):
        return x * y

    # Define a method for division that takes two arguments and returns the result if the denominator is not zero,
    # or an error message if the denominator is zero
    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return ("Cannot divide by zero.")

# Example usage
# Create an instance of the Calculator class
calculator = Calculator()

# Perform addition and print the result
result = calculator.add(7, 5)
print("7 + 5 =", result)

# Perform subtraction and print the result
result = calculator.subtract(34, 21)
print("34 - 21 =", result)

# Perform multiplication and print the result
result = calculator.multiply(54, 2)
print("54 * 2 =", result)

# Perform division and print the result
result = calculator.divide(144, 2)
print("144 / 2 =", result)

# Attempt to perform division by zero, which raises an error, and print the error message
result = calculator.divide(45, 0)
print("45 / 0 =", result)

#4. Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.

# Import the math module to access mathematical functions like pi
import math

# Define a base class called Shape to represent a generic shape with methods for calculating area and perimeter
class Shape:
    # Placeholder method for calculating area (to be implemented in derived classes)
    def calculate_area(self):
        pass

    # Placeholder method for calculating perimeter (to be implemented in derived classes)
    def calculate_perimeter(self):
        pass

# Define a derived class called Circle, which inherits from the Shape class
class Circle(Shape):
    # Initialize the Circle object with a given radius
    def __init__(self, radius):
        self.radius = radius

    # Calculate and return the area of the circle using the formula: π * r^2
    def calculate_area(self):
        return math.pi * self.radius**2

    # Calculate and return the perimeter of the circle using the formula: 2π * r
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

# Define a derived class called Rectangle, which inherits from the Shape class
class Rectangle(Shape):
    # Initialize the Rectangle object with given length and width
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Calculate and return the area of the rectangle using the formula: length * width
    def calculate_area(self):
        return self.length * self.width

    # Calculate and return the perimeter of the rectangle using the formula: 2 * (length + width)
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# Define a derived class called Triangle, which inherits from the Shape class
class Triangle(Shape):
    # Initialize the Triangle object with a base, height, and three side lengths
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    # Calculate and return the area of the triangle using the formula: 0.5 * base * height
    def calculate_area(self):
        return 0.5 * self.base * self.height

    # Calculate and return the perimeter of the triangle by adding the lengths of its three sides
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

# Example usage
# Create a Circle object with a given radius and calculate its area and perimeter
r = 7
circle = Circle(r)
circle_area = circle.calculate_area()
circle_perimeter = circle.calculate_perimeter()

# Print the results for the Circle
print("Radius of the circle:", r)
print("Circle Area:", circle_area)
print("Circle Perimeter:", circle_perimeter)

# Create a Rectangle object with given length and width and calculate its area and perimeter
l = 5
w = 7
rectangle = Rectangle(l, w)
rectangle_area = rectangle.calculate_area()
rectangle_perimeter = rectangle.calculate_perimeter()

# Print the results for the Rectangle
print("\nRectangle: Length =", l, " Width =", w)
print("Rectangle Area:", rectangle_area)
print("Rectangle Perimeter:", rectangle_perimeter)

# Create a Triangle object with a base, height, and three side lengths, and calculate its area and perimeter
base = 5
height = 4
s1 = 4
s2 = 3
s3 = 5

# Print the results for the Triangle
print("\nTriangle: Base =", base, " Height =", height, " side1 =", s1, " side2 =", s2, " side3 =", s3)
triangle = Triangle(base, height, s1, s2, s3)
triangle_area = triangle.calculate_area()
triangle_perimeter = triangle.calculate_perimeter()
print("Triangle Area:", triangle_area)
print("Triangle Perimeter:", triangle_perimeter)

#5. In computer science, a binary search tree (BST), also called an ordered or sorted binary tree, is a rooted binary tree data structure with the key of each internal node being greater than all the keys in the respective node's left subtree and less than the ones in its right subtree. The time complexity of operations on the binary search tree is directly proportional to the height of the tree.

# Binary search tree:
# In computer science, a binary search tree (BST), also called an ordered or sorted binary tree, is a rooted binary tree data structure with the key of each internal node being greater than all the keys in the respective node's left subtree and less than the ones in its right subtree. The time complexity of operations on the binary search tree is directly proportional to the height of the tree.

# Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.

# Define a class called Node to represent a node in a binary search tree (BST)
class Node:
    # Initialize the Node object with a value, and set the left and right child pointers to None
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Define a custom __str__ method to convert the node's value to a string
    def __str__(self):
        return str(self.value)

# Define a class called BinarySearchTree to represent a binary search tree
class BinarySearchTree:
    # Initialize the BST with an empty root node
    def __init__(self):
        self.root = None

    # Insert a value into the BST
    def insert(self, value):
        # If the root is None, create a new node with the given value as the root
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    # Helper method to recursively insert a value into the BST
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    # Search for a value in the BST
    def search(self, value):
        return self._search_recursive(self.root, value)

    # Helper method to recursively search for a value in the BST and return the node if found
    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

# Example usage
# Create an instance of BinarySearchTree
bst = BinarySearchTree()

# Insert values into the BST
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

# Search for elements in the BST and print the results
print("Searching for elements:")
print(bst.search(4))  # Found, returns the node (4)
print(bst.search(9))  # Not found, returns None 

#6. Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.

# Define a class called Stack to implement a stack data structure
class Stack:
    # Initialize the stack with an empty list to store items
    def __init__(self):
        self.items = []

    # Push an item onto the stack
    def push(self, item):
        self.items.append(item)

    # Pop (remove and return) an item from the stack if the stack is not empty
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Cannot pop from an empty stack."

    # Check if the stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Get the number of items in the stack
    def size(self):
        return len(self.items)

    # Peek at the top item of the stack without removing it, if the stack is not empty
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Empty stack."

# Example usage
# Create an instance of the Stack class
stack = Stack()

# Push items onto the stack
stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

# Print the size of the stack and the top element
print("Stack size:", stack.size())
print("Top element:", stack.peek())

# Pop an item from the stack, and print the popped item, and the updated size and top element
popped_item = stack.pop()
print("\nPopped item:", popped_item)
print("\nStack size:", stack.size())
print("Top element:", stack.peek())

#----------------------------------------
# Create another instance of the Stack class
stack1 = Stack()

# Print the size of the empty stack and attempt to pop an item (with an error message)
print("\nStack size:", stack1.size())
popped_item = stack1.pop()
print("\nPopped item:", popped_item) 

#7 Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting and deleting nodes.

# Define a class called Node to represent a node in a linked list
class Node:
    # Initialize the Node object with data and set the next pointer to None
    def __init__(self, data):
        self.data = data
        self.next = None

# Define a class called LinkedList to represent a singly linked list
class LinkedList:
    # Initialize the linked list with an empty head node
    def __init__(self):
        self.head = None

    # Display the elements in the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    # Insert a new node with the given data at the end of the linked list
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Delete a node with the given data from the linked list
    def delete(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current:
            prev.next = current.next

# Example usage
# Create an instance of the LinkedList class
linked_list = LinkedList()

# Insert elements into the linked list
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)

# Display the initial linked list
print("Initial Linked List:")
linked_list.display()

# Insert a new node with data 5 into the linked list
linked_list.insert(5)
print("After inserting a new node (5):")
linked_list.display()

# Delete a node with data 2 from the linked list
linked_list.delete(2)
print("After deleting an existing node (2):")
linked_list.display() 

#8 Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.

# Define a class called ShoppingCart to represent a shopping cart
class ShoppingCart:
    # Initialize the shopping cart with an empty list of items
    def __init__(self):
        self.items = []

    # Add an item with a name and quantity to the shopping cart
    def add_item(self, item_name, qty):
        item = (item_name, qty)
        self.items.append(item)

    # Remove an item with a specific name from the shopping cart
    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    # Calculate and return the total quantity of items in the shopping cart
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total

# Example usage
# Create an instance of the ShoppingCart class
cart = ShoppingCart()

# Add items to the shopping cart
cart.add_item("Papaya", 100)
cart.add_item("Guava", 200)
cart.add_item("Orange", 150)

# Display the current items in the cart and calculate the total quantity
print("Current Items in Cart:")
for item in cart.items:
    print(item[0], "-", item[1])

total_qty = cart.calculate_total()
print("Total Quantity:", total_qty)

# Remove an item from the cart, display the updated items, and recalculate the total quantity
cart.remove_item("Orange")
print("\nUpdated Items in Cart after removing Orange:")
for item in cart.items:
    print(item[0], "-", item[1])

total_qty = cart.calculate_total()
print("Total Quantity:", total_qty) 

#9 Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping and displaying elements.

# Define a class called Stack to implement a stack data structure
class Stack:
    # Initialize the stack with an empty list to store items
    def __init__(self):
        self.items = []

    # Push an item onto the stack
    def push(self, item):
        self.items.append(item)

    # Pop (remove and return) an item from the stack if the stack is not empty
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Cannot pop from an empty stack.")

    # Check if the stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Display the items in the stack
    def display(self):
        print("Stack items:", self.items)

# Example usage
# Create an instance of the Stack class
stack = Stack()

# Push items onto the stack
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

# Display the items in the stack
stack.display()

# Pop items from the stack and print the popped items
popped_item = stack.pop()
print("Popped item:", popped_item)
popped_item = stack.pop()
print("Popped item:", popped_item)

# Display the updated items in the stack
stack.display()

#10 Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.

# Define a class called Queue to implement a queue data structure
class Queue:
    # Initialize the queue with an empty list to store items
    def __init__(self):
        self.items = []

    # Add (enqueue) an item to the end of the queue
    def enqueue(self, item):
        self.items.append(item)

    # Remove and return (dequeue) an item from the front of the queue if the queue is not empty
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Cannot dequeue from an empty queue.")

    # Check if the queue is empty
    def is_empty(self):
        return len(self.items) == 0

# Example usage
# Create an instance of the Queue class
queue = Queue()

# Enqueue (add) items to the queue
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

# Print the current items in the queue
print("Current Queue:", queue.items)

# Dequeue (remove) items from the front of the queue and print the dequeued items
dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)
dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)

# Print the updated items in the queue
print("Updated Queue:", queue.items) 

#11 Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.

# Define a class called Bank to implement a simple banking system
class Bank:
    # Initialize the bank with an empty dictionary to store customer accounts and balances
    def __init__(self):
        self.customers = {}

    # Create a new account with a given account number and an optional initial balance (default to 0)
    def create_account(self, account_number, initial_balance=0):
        if account_number in self.customers:
            print("Account number already exists.")
        else:
            self.customers[account_number] = initial_balance
            print("Account created successfully.")

    # Make a deposit to the account with the given account number
    def make_deposit(self, account_number, amount):
        if account_number in self.customers:
            self.customers[account_number] += amount
            print("Deposit successful.")
        else:
            print("Account number does not exist.")

    # Make a withdrawal from the account with the given account number
    def make_withdrawal(self, account_number, amount):
        if account_number in self.customers:
            if self.customers[account_number] >= amount:
                self.customers[account_number] -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient funds.")
        else:
            print("Account number does not exist.")

    # Check and print the balance of the account with the given account number
    def check_balance(self, account_number):
        if account_number in self.customers:
            balance = self.customers[account_number]
            print(f"Account balance: {balance}")
        else:
            print("Account number does not exist.")

# Example usage
# Create an instance of the Bank class
bank = Bank()

# Create customer accounts and perform account operations
acno1= "SB-123"
damt1 = 1000
print("New a/c No.: ",acno1,"Deposit Amount:",damt1)
bank.create_account(acno1, damt1)

acno2= "SB-124"
damt2 = 1500
print("New a/c No.: ",acno2,"Deposit Amount:",damt2)
bank.create_account(acno2, damt2)

wamt1 = 600
print("\nDeposit Rs.",wamt1,"to A/c No.",acno1)
bank.make_deposit(acno1, wamt1)

wamt2 = 350
print("Withdraw Rs.",wamt2,"From A/c No.",acno2)
bank.make_withdrawal(acno2, wamt2)

print("A/c. No.",acno1)
bank.check_balance(acno1)

print("A/c. No.",acno2)
bank.check_balance(acno2)

wamt3 = 1200
print("Withdraw Rs.",wamt3,"From A/c No.",acno2)
bank.make_withdrawal(acno2, wamt3)

acno3 = "SB-134"
print("A/c. No.",acno3)
bank.check_balance(acno3)  # Non-existent account number 