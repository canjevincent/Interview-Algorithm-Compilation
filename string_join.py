# def count_sheep(n):
#     return ''.join(f"{i} sheep..." for i in range(1,n+1))

# def reverse_words(str):
#     return ' '.join(s[::-1] for s in str.split(' '))

# def printer_error(s):
#     return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))

# def connect_words(word):

#   return " ".join(str(x) for x in word)

# print(connect_words(['hello','world','this','is','great']))

# def connect_words(word):

#   return " ".join(word)

# print(connect_words(['hello','world','this','is','great']))

# def disemvowel(string):
#     return "".join(c for c in string if c.lower() not in "aeiou")

# def string_to_array(s):

#   return [l for l in s.split(' ')]

# print(string_to_array("1 2 3"))

# -=-=--

# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

# Write a function which takes a list of strings and returns each line prepended by the correct number.

# The numbering starts at 1. The format is n: string. Notice the colon and space in between.

# Examples: (Input --> Output)

# [] --> []

# ["a", "b", "c"] --> ["1: a", "2: b", "3: c"]

# def number(lines):
#   return ['%d: %s' % v for v in enumerate(lines, 1)]

# def number(lines):
#     return [f"{counter}: {line}" for counter, line in enumerate(lines, start=1)]

# def number(lines):
#     return ['{}: {}'.format(n, s) for (n, s) in enumerate(lines, 1)]

# def strCount(string, letter):
#     return string.count(letter)

# print(strCount('five','i'))

# def count_by(x, n):
#     """
#     Return a sequence of numbers counting by `x` `n` times.
#     """
#     return range(x, x * n + 1, x)

# def get_grade(s1, s2, s3):
#     m = (s1 + s2 + s3) / 3.0
#     if 90 <= m <= 100:
#         return 'A'
#     elif 80 <= m < 90:
#         return 'B'
#     elif 70 <= m < 80:
#         return 'C'
#     elif 60 <= m < 70:
#         return 'D'
#     return "F"

# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

# Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
# Note: For 4 or more names, the number in "and 2 others" simply increases.

# def likes(names):
#     n = len(names)
#     return {
#         0: 'no one likes this',
#         1: '{} likes this', 
#         2: '{} and {} like this', 
#         3: '{}, {} and {} like this', 
#         4: '{}, {} and {others} others like this'
#     }[min(4, n)].format(*names[:3], others=n-2)

# def likes(names):
#     if len(names) == 0:
#         return "no one likes this"
#     elif len(names) == 1:
#         return "%s likes this" % names[0]
#     elif len(names) == 2:
#         return "%s and %s like this" % (names[0], names[1])
#     elif len(names) == 3:
#         return "%s, %s and %s like this" % (names[0], names[1], names[2])
#     else:
#         return "%s, %s and %s others like this" % (names[0], names[1], len(names)-2)


# def double_char(s):
    
#     return ''.join(x+x for x in s) 

# print(double_char('qwe')) 

def find_short(s):

  return min( len(x) for x in s.split() )

print(find_short('bitcoin take over the world maybe who knows perhaps'))



# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

# Examples
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
# ""  -->  ""

def order(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))