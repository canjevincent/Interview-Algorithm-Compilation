def binary_search(arr, target):

  # Get the current upper and lower bounds
  lo = 0
  hi = len(arr)-1

  # If lo > hi, then the value is not in the array
  while lo <= hi:

    # Find the midpoint
    mid = (hi + lo) // 2

    print("1st hi: "+str(hi),"lo: "+str(lo),"mid: "+str(mid))

    # If the value is the one we're looking for, return index
    if arr[mid] == target:
      return mid

    # If value is greater than target, update hi so that we only look
    # at the lower half of the array
    if arr[mid] > target:
      hi = mid-1

    # Otherwise look at the greater half of the array
    else:
      lo = mid+1

    print("2nd hi: "+str(hi),"lo: "+str(lo),"mid: "+str(mid))  
  
  #  We didn't find the value in the array so return -1
  return -1

print(binary_search([1,2,3,4,5,6,7,8],2))