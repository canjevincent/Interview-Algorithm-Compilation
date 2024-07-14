
# Python program to demonstrate working
# of map.
  
# Return double of n
def addition(n):
    return n + n
  
# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

def sum_mix(arr):
    return sum(map(int, arr))

# Double all numbers using map and lambda
  
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

# Add two lists using map and lambda
  
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
  
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))


def digitize(n):
    return map(int, str(n)[::-1])

def digitize(n):
    return [int(x) for x in str(n)[::-1]]



def sum_two_lowest_num(arr):

  arr.sort()

  return arr[0] + arr[1]

print(sum_two_lowest_num([5,4,3,2,1]))
