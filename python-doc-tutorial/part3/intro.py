# string keep raw formatting
# way 1: raw string
print(r'C:\some\name')

# way 2: triple quotes:
# the backslash prevent the default behavior: End of lines are automatically included in the string
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to \
""")

# string concat
print(3 * 'un' + 'ium')
print('Py' 'thon')  # this not apply with variable => using + to concat
prefix = 'Py'
print(prefix * 3 + 'thon')

#  string index
#  P  y  t  h  o  n
#  0  1  2  3  4  5
# -6 -5 -4 -3 -2 -1
word = 'Python'

# string slice: str_object[start_pos:end_pos:step]
# start_pos default value is 0, the end_pos default value is the length of string and step default value is 1
#  if step < 0 => start_pos > end_pos

word[2:5]  # characters from position 2 (included) to 5 (excluded)
# 'tho

# characters from position 2 (included) to 5 (excluded) and step = 2
word[2:5:2]
# 'to

word[:2]   # character from the beginning to position 2 (excluded)
# 'Py'

word[4:]   # characters from position 4 (included) to the end
# 'on'

word[-2:]  # characters from the second-last (included) to the end
# 'on'

# reverse string
print(word[::-1])  # backtrack 1 character

# word[0] = 'd' # error because 'str' object is immutable

# ----------------------------------------------------------------
# list
squares = [1, 4, 9, 16, 25]
squares[:]  # slicing returns a new list :  a shallow copy of the list


# swap variable:
a, b = 0, 1
a, b = b, a
