def summation(num):
    return sum(xrange(num + 1))

def summation(num):
    return sum(range(1,num+1))

def summation(num):
    return (1+num) * num / 2

def summation(num):

  nums = 0

  for x in range(1,num+1):

    nums += x
  
  return nums

print(summation(10))
