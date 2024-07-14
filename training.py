# def StringChallenge(new_str):

#   param_remove_duplicate = set(new_str)

#   current_param = list(new_str)
#   loop_len = len(new_str)
#   check_index = 0

#   while loop_len != 0:

#     if len(set(current_param)) == 1:
#       break
  
#     if loop_len > 1:
#       if current_param[check_index] != current_param[check_index+1]:

#         replacement_letter = param_remove_duplicate.difference([current_param[check_index],current_param[check_index+1]])
#         del current_param[check_index]
#         del current_param[check_index]
#         current_param = list(replacement_letter) + current_param

#         loop_len -= 1
#         check_index = 0
#         continue

#       else:

#         loop_len += 1
#         check_index += 1
#         continue
  
  # return len(current_param)

# print(StringChallenge("abcabc"))

# def MissingDigit(new_str):
  
  # Initialize a variable " x " to store the value of the missing digit
  # x = 0

  # Replace the " x " character in the input string with the value of x (which is 0)
  # This is done using the replace() function

  # temp = new_str.replace("x", str(x))

  # Split the modified string into an array containing the two sides of the equation
  # This is done using the split() function with " = " as the delimiter

  # arr = temp.split(" = ")

  # Use a while loop to iterate through possible values of " x " (0 to 9)
  # Keep looping until the left side of the question is equal to the right side

  # while eval(arr[0]) != eval(arr[1]):
    
    # Increment the value of " x " by 1

    # x+=1

    # Replace the " x " character in the input string with the updated value of " x "

    # temp = new_str.replace("x", str(x))

    # Split the updated string into an array containing the two sides of the equation

#     arr = temp.split(" = ")

#   return x

# print(MissingDigit("4 - 2 = x"))

# You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would make this happen, return -1.

# For example:

# Let's say you are given the array {1,2,3,4,3,2,1}:
# Your function will return the index 3, because at the 3rd position of the array, the sum of left side of the index ({1,2,3}) and the sum of the right side of the index ({3,2,1}) both equal 6.

# Let's look at another one.
# You are given the array {1,100,50,-51,1,1}:
# Your function will return the index 1, because at the 1st position of the array, the sum of left side of the index ({1}) and the sum of the right side of the index ({50,-51,1,1}) both equal 1.

# Last one:
# You are given the array {20,10,-80,10,10,15,35}
# At index 0 the left side is {}
# The right side is {10,-80,10,10,15,35}
# They both are equal to 0 when added. (Empty arrays are equal to 0 in this problem)
# Index 0 is the place where the left side and right side are equal.

# Note: Please remember that in most programming/scripting languages the index of an array starts at 0.

# Input:
# An integer array of length 0 < arr < 1000. The numbers in the array can be any integer positive or negative.

# Output:
# The lowest index N where the side to the left of N is equal to the side to the right of N. If you do not find an index that fits these rules, then you will return -1.

# Note:
# If you are given an array with multiple answers, return the lowest correct index.


# Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

# For example, a tower with 3 floors looks like this:

# [
#   "  *  ",
#   " *** ", 
#   "*****"
# ]
# And a tower with 6 floors looks like this:

# [
#   "     *     ", 
#   "    ***    ", 
#   "   *****   ", 
#   "  *******  ", 
#   " ********* ", 
#   "***********"
# ]

# def tower_builder(n):
#     return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]

# print(list('qweasdf'))

# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

# Note: input will never be an empty string

# def fake_bin(x):
    
#     z = []

#     for a in range(len(x)):

#       y = ''

#       for b in x[a]:
#         if int(b) < 5:
#           y += '0'
#         if int(b) >= 5:
#           y += '1'
      
#       z.append(y)
    
#     return z

# print(fake_bin(["45385593107843568","509321967506747","366058562030849490134388085","15889923","800857237867"]))


# print(sorted(set('AAAABBBCCDAABBB')))

# def check_position(position):

#   ps = []
  
#   for x in range(len(position)):

#     ps.append(x)
  
#   return ps


# print(check_position(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]))

# text = "Python is easy to learn."

# result = text.endswith('to learn')
# # returns False
# print(result)

# result = text.endswith('to learn.')
# # returns True
# print(result)

# result = text.endswith('Python is easy to learn.')
# # returns True
# print(result)


# def check_equality(test, original):

#     return list('asdasdsadzxczxczxvzxvasd weqweqwe')

# print(check_equality('Qqqwweerrr','Rrrqqqwwee'))

# def sum_val(a,b):
#   return f'X = {int(a)+int(b)}'

# a = input()
# b = input()

# print(sum_val(a,b))

# def aoc(a):
#     return f'A = { "{:.4f}".format( ( 3.14159 * float(a) ) ** 2 ) }'

# a = input()

# print(aoc(a))

# def reverse_string(a):
#   b = a.split()
#   b.reverse()
#   return b

# print(reverse_string('Hello World'))

# def reverse_string(a):
    
#     return range(1,len(a))


# print(reverse_string(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']))



# pairs = {'A':'T','T':'A','C':'G','G':'C'}
# def DNA_strand(dna):
#     return ''.join([pairs[x] for x in dna])

# print([x for x in range(1,5+1)]).remove(1)


# def shortcut(s):

#   r = ['a','e','i','o','u']

#   return [x for x in s if x not in r]

# print(shortcut("qwer"))

# print('qwer'[::-1])


# def solve(n):

#   return [x for x in str(n)]

# print(solve(123456))

# This is a demo task.

# Write a function:

# def solution(A)

# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].
# Copyright 2009–2022 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

# def solution(N):
    
#     n_w = []

#     for x in list(str(N)):

#       if min(list(str(N))) == str(x):

#         n_w.append(5)
#         n_w.append(int(x))
      
#       else:

#         n_w.append(int(x))

#     return "".join(str(a) for a in n_w)

# print(solution(268))

# def algo(N):

#   rd = None
#   ld = None
#   total_arr_len = [x for x in range(len(N))]

#   for x in range(len(N)):

#     if (x-1) < 0:
      
#       ld = 0
#       rd = 0

#       for a in range(len(N)):
        
#         if a > x:

#           rd += N[a]

#       if ld == rd:

#         return N[x]

#     else:

#       ld = 0
#       rd = 0
      
#       for b in range(len(N)):

#         if b > x:

#           rd += N[b]
      
#       for c in range(len(N)):

#         if c < x:

#           ld += N[c]
      
#       if ld == rd:

#         return N[x]

# print(algo([20,10,-80,10,10,15,35]))

# def check_range(N):
  
  # total_arr_len = [x for x in range(len(N))]

  # return min(total_arr_len)

#   for x in range(len(N)):

#     print(x)

# print(check_range([1,2,3,4,3,2,1]))

# def reverse(S):
    
#   print(list(S), "COMPLETE")
#   print(list(S)[2:], "2:")
#   print(list(S)[:2], ":2")

# reverse("REVERSE")

# def dreverse(S):
    
#   print(S[::-1])

# dreverse([1,2,3,4,5,6,7,8,9,10])
# dreverse([2,4,6,8,10,12,14,16,18,20])

# [int(x) for x in str(N)]

# GET THE MAX VALUE FROM DICTIONARY

# max(check_count.values())

# GET THE KEY FROM DICTIONARY HIGHEST VALUE

# max(check_count,key=check_count.get)

# GET BOTH KEY AND VALUE

# for i, x in enumerate(a):

# (11) def increment_string(strng):
    
#     # strip the decimals from the right
#     stripped = strng.rstrip('1234567890')
    
#     # get the part of strng that was stripped
#     ints = strng[len(stripped):]
    
#     if len(ints) == 0:
#         return strng + '1'
#     else:
#         # find the length of ints
#         length = len(ints)
    
#         # add 1 to ints
#         new_ints = 1 + int(ints)
    
#         # pad new_ints with zeroes on the left
#         new_ints = str(new_ints).zfill(length)
    
#         return stripped + new_ints


# def atMostSum(arr, n, k):
#     _sum = 0
#     cnt = 0
#     maxcnt = 0
     
#     for i in range(n):
        
#         print("- ",i,"range count -")
 
#         # If adding current element doesn't
#         # Cross limit add it to current window
#         if (_sum + arr[i]) <= k:
#             _sum += arr[i]
#             cnt += 1

#             print(cnt,_sum," first")
         
#         # Else, remove first element of current
#         # window and add the current element
#         elif(_sum != 0):
            
#             print(_sum,"-",i,cnt,"-",arr[i - cnt],arr[i]," mid")
            
#             _sum = _sum - arr[i - cnt] + arr[i]
        
#             print(cnt,_sum," second")

#         # keep track of max length.
#         maxcnt = max(cnt, maxcnt)
 
#     return maxcnt
     
# # Driver function
# arr = [1, 2, 1, 0, 1, 1, 0]
# n = len(arr)
# k = 4

# print(atMostSum(arr, n, k))

# def reverse_alpha(l):

#   new_letter = ""

#   reversed_all_letter = [x for x in reversed(l) if x.isalpha()] 

#   ctr_len = 0

#   for a, b in enumerate(l):

#     if b.isalpha():
      
#       new_letter += reversed_all_letter[ctr_len]
#       ctr_len += 1

#     else:

#       new_letter += l[a]

#   print(new_letter)

# reverse_alpha("a-bC-dEf=ghIj!!")

# def find_subarray_less_k(a,b):

#   max_set_len = []

#   for x in range(len(a)):

#     if a[x] < b:

#       max_set_len.append(a[x])

#     set_num_arr = []

#     for y in range(x, len(a)):

#       if (sum(set_num_arr) + a[y]) < b:

#         set_num_arr.append(a[y])
      
#       else:

#         break

#     if len(set_num_arr) > 1 and set_num_arr not in max_set_len:
      
#       max_set_len.append(set_num_arr)
  
#   print(len(max_set_len))

# find_subarray_less_k([1, 11, 2, 3, 15],10)

# def subarr_range(arr_set, l, r):

#   find_set = []

#   for x in range(len(arr_set)):

#     if arr_set[x] >= l and arr_set[x] <= r:
        
#       find_set.append(arr_set[x])

#     for y in range(x,len(arr_set)):

#       sum_arr_set = []

#       for k in range(x,y+1):
        
#         if len(sum_arr_set) > 0:

#           if (sum(sum_arr_set) + arr_set[k]) >= l and (sum(sum_arr_set) + arr_set[k]) <= r:
            
#             sum_arr_set.append(arr_set[k])
          
#           else:

#             break
        
#         else:

#           sum_arr_set.append(arr_set[k])
      
#       if sum_arr_set not in find_set and len(sum_arr_set) != 1 and sum(sum_arr_set) != 0:

#         find_set.append(sum_arr_set)
    
#   print(len(find_set), find_set)

# subarr_range([1, 4, 6], 3, 8)

# def find_sub_sum_least_max(set_arr[], k):

#   max_arr_sum 

#   for x in range(len(set_arr)):



# find_sub_sum_least_max([2, 4, 5, 1, 4, 6, 6, 2, 1, 0], 3)

# def max_sum_arr_test(arr_set):
    
#   max_sum, cur_sum = float("-inf"), 0

#   for n in arr_set:

#     cur_sum = max(cur_sum+n,n)
#     max_sum = max(max_sum,cur_sum)
  
#   print(max_sum)

# max_sum_arr_test([-2,1,-3,4,-1,2,1,-5,4])


# def half_max_sum_sub_array(arr_set, k):
    
#     max_arr_sum = float("-inf")

#     for x in range(len(arr_set)):

#       max_arr_len = []

#       for y in range(x,len(arr_set)):
         
#         if len(max_arr_len) == k:

#           max_arr_sum = max(max_arr_sum,sum(max_arr_len))
#           break

#         else:
           
#           max_arr_len.append(arr_set[y])
    
#     max_arr_equal_sum = float("inf")
#     max_arr_equal_sum_len = []

#     for a in range(len(arr_set)):

#       max_arr_equal_len = []

#       for b in range(a,len(arr_set)):
        
#         if len(max_arr_equal_len) == k and sum(max_arr_equal_len) >= (max_arr_sum/2):

#             if sum(max_arr_equal_len) < max_arr_equal_sum:

#               max_arr_equal_sum_len.clear()
#               max_arr_equal_sum_len.extend(max_arr_equal_len)

#             max_arr_equal_sum = min(max_arr_equal_sum,sum(max_arr_equal_len))

#             break

#         else:
           
#           max_arr_equal_len.append(arr_set[b])
    
#     print(max_arr_equal_sum, max_arr_equal_sum_len)

# half_max_sum_sub_array([12, 45, 11, 10, 8, 56, 2], 4)

# def count_negative_element_arr(set_arr, k):

#   arr_neg_num = []

#   for x in range(len(set_arr)):

#     arr_neg_num_set = []

#     for y in range(x,len(set_arr)):

#       if len(arr_neg_num_set) == k:
      
#         break
      
#       else:
      
#         arr_neg_num_set.append(set_arr[y])
    
#     if len(arr_neg_num_set) == k:

#       arr_neg_num_set = [n for n in arr_neg_num_set if n < 0]

#       arr_neg_num.append(len(arr_neg_num_set))

#     else:

#       break
  
#   print(arr_neg_num)

# count_negative_element_arr([-1, 2, 4, 4],2)

# def sum_min_max_arr(set_arr, k):
    
#     set_max_min_sum_arr = []

#     for x in range(len(set_arr)):
        
#       max_min_arr_len = []
#       max_min_arr_len_set = 0

#       for y in range(x,len(set_arr)):
         
#         if len(max_min_arr_len) == k:
#           break
#         else:
#           max_min_arr_len.append(set_arr[y])
      
#       if len(max_min_arr_len) == k:
#         max_min_arr_len_set = max(max_min_arr_len) + min(max_min_arr_len)
#       else:
#         continue

#       set_max_min_sum_arr.append(max_min_arr_len_set)
    
#     print(sum(set_max_min_sum_arr))

# sum_min_max_arr([2, 5, -1, 7, -3, -1, -2], 4)

# def sum_min_max_arr(set_arr, k):
    
    # set_max_min_sum_arr = []

    # for x in range(len(set_arr)):
        
    #   max_min_arr_len = []
    #   max_min_arr_len_set = 0

    #   for y in range(x,len(set_arr)):
         
    #     if len(max_min_arr_len) == k:
    #       break
    #     else:
    #       max_min_arr_len.append(set_arr[y])
      
    # print(sum(set_max_min_sum_arr))

# sum_min_max_arr([2, 5, -1, 7, -3, -1, -2], 4)

# PRINT ALL POSSIBLE SUbARRAY RECURSIVE
# def printSubsets(lst, toggles=None, i=0):
    
#     if toggles == None:
#         toggles = [0] * len(lst)
    
#     if i >= len(lst):
#         subset = [str(lst[i]) for i in range(len(lst)) if toggles[i] == 1]
#         print("{" + ", ".join(subset) + "}")
#     else:
#         toggles[i] = 0
#         printSubsets(lst, toggles, i+1)
#         toggles[i] = 1
#         printSubsets(lst, toggles, i+1)

# printSubsets([2, 5, -1, 7, -3, -1, -2])

# def printSubsequences(arr, index, subarr):
       
#     # Print the subsequence when reach 
#     # the leaf of recursion tree
#     if index == len(arr):
           
#         # Condition to avoid printing
#         # empty subsequence
#         if len(subarr) != 0:
#             print(subarr)
       
#     else:
#         # Subsequence without including 
#         # the element at current index
#         printSubsequences(arr, index + 1, subarr)
           
#         # Subsequence including the element
#         # at current index
#         printSubsequences(arr, index + 1, 
#                             subarr+[arr[index]])
       
#     return
           
# arr = [2, 5, -1, 7, -3, -1, -2]
   
# printSubsequences(arr, 0, [])

# def generate_subsequences(arr):
  
#   n = len(arr)
#   subsequences = [[]]

#   for i in range(n):
  
#     for j in range(len(subsequences)):
  
#       current_subsequence = subsequences[j]
  
#       subsequences.append(current_subsequence + [arr[i]])
  
#   return subsequences

# arr = [1,2,3,4]
# subsequences = generate_subsequences(arr)

# print(subsequences)


# check_arr = [1,2,3,4,5,6,7,8,9,10]
# new_set = list(reversed(check_arr))

# def missing_int(A):

#   num = 0

#   for x in range(min(A), max(A)+1):

#     if x not in A:
#       num = x
#       break
  
#   else:

#     num = max(A) + 1

#   return 1 if min(A) < 0 and max(A) < 0 else num

# print(missing_int([1, 3, 6, 4, 1, 7, 8, 10]))

# def find_divisible(a, b, k):

#   count_div = 0

#   for x in range(a,b+1):

#     if (x % k) == 0:
#       count_div += 1
  
#   return count_div

# print(find_divisible(0,11,2))

# def rotate(A, k):

#   for i in range(0, k):

#     temp = A[len(A)-1] 

#     for j in range(len(A)-1, 0, -1):

#       A[j] = A[j-1]

#     A[0] = temp

#   return A  

# print(rotate([1, 2, 3, 4], 4))

# def find_prime(n):

#   all_num = []

#   for x in range(n):

#     if x > 1:

#       for y in range(2,x):

#         if (x % y) == 0:
#           break
      
#       else:
#           all_num.append(x)

#   new_str = [str(a) for a in all_num]
  
#   print(" ".join(new_str))

# find_prime(100)


  