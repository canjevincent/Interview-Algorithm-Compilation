# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# newlist = [x for x in range(10) if x < 5]

# newlist = [x if x != "banana" else "orange" for x in fruits]

# print(newlist)

# def reverse_seq(n):

#   return list(reversed([x for x in range(1,n+1)]))

# print(reverse_seq(5))

# Reverse Range
# x = range(10, 0, -1)

# for n in x:
#   print(n)

# if condition on the middle with else
# if condition on last without else

# def friend(x):
#     return [f for f in x if len(f) == 4]

# SUM OF ODD NUMBERS

# def sum_odd_number(n):
#     return n**3

# You are given an odd-length array of integers, in which all of them are the same, except for one single number.

# Complete the method which accepts such an array, and returns that single different number.

# The input array will always be valid! (odd-length >= 3)

# def stray(arr):
#     for x in arr:
#         if arr.count(x) == 1:
#             return x

# def stray(arr):
#     for x in set(arr):
#         if arr.count(x) == 1: return x

def array_mult(a):

  return [int(x) for x in str(a)]

print(array_mult(123))

# Return the min number not in array

# def min_num(num):

#   sort_arr = sorted(num)

#   new_num = 0

#   for x in range(len(num)):

#     if (x+1) in [x for x in range(len(num))]:
    
#       if sort_arr[x] != (sort_arr[x+1] - 1):
        
#         new_num += sort_arr[x] + 1

#         break
    
#     else:

#       new_num += sort_arr[x] + 1
  
#   print(new_num)

# min_num([1,2,3,4,20,50])

# Return all divisble
# def divisible(num):

#   print( list(filter(None, [x if (num % x) == 0 else None for x in range(2,num)])) )

# divisible(21)

# Check if num is a prime, only divisible by 1 and itself
# def prime(num):

#   check_prime = True

#   for x in range(2,num):

#     if (num % x) == 0:
#       check_prime = False
#       break
  
#   print(check_prime)

# prime(21)