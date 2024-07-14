# def basic_op(operator, value1, value2):
#     return eval("{}{}{}".format(value1, operator, value2))

# def get_middle(s):
#     index, odd = divmod(len(s), 2)
#     return s[index] if odd else s[index - 1:index + 1]
    
# print(get_middle('dinosaur'))

# def is_uppercase(inp):
#     return inp.upper()==inp

# def correct(string):

#     cor=''
#     for leter in string:
#       if leter =='1':
#         cor+='I'
#       elif leter=='5':
#         cor+='S'
#       elif leter=='0':
#         cor+='O'
#       else:
#         cor+=leter
#     return cor

# print(correct('1F-RUDYARD K1PL1NG'))

# def remove_every_other(my_list):

#   o, t = 1, 1

#   num = ""

#   for x in my_list:

#     num += str(x)
    
#   return o + t

# print(remove_every_other([153, 154, 158, 124, 136, 147]))


# def check_string(string):

#   w_string = ""

#   for x in string.split():

#     n_string = ""

#     for y in range(len(list(x))):

#       if y == 0:
#         n_string+= list(x)[y].upper()
#       else:
#         n_string+= list(x)[y]

#     w_string += n_string+" " 
      
#   return w_string

# print(check_string("How can mirrors be real if our eyes aren't real"))

# def check_string(string):

#   w_string = ""

#   for x in string.split():

#     n_string = ""

#     for y in range(len(list(x))):

#       if y == 0:
#         n_string += list(x)[y].upper()
#       else:
#         n_string += list(x)[y]

# print(check_string("How can mirrors be real if our eyes aren't real"))


def check_val(n):
  
  # arr = []

  # for x in range(n):

  #   arr.append(x**2)

  # return arr

  ctr_val = 0
  ctr_loop = n
  ctr_arr = []

  while ctr_loop != 0:
    
    ctr_val += (ctr_val + 1)
    ctr_arr.append(ctr_val)
    ctr_loop -= 1
  
  return ctr_arr

print(check_val(10))


