# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# duplicates not allowed

print( len("step") == len( set("step".lower()) ) )

def find_uniq(arr):
    
    a, b = set(arr)
    
    return a if arr.count(a) == 1 else b

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))