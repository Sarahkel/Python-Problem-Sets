# Sarah Scholz 10/02/2018 
# Taken from: https://github.com/ianmcloughlin/python-fib/blob/master/fibname.py
# A program that displays Fibonacci numbers using people's names.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Scholz"
# my surname
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
# for definition of this function see below (line 47 onwards)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)


# Forum Post EXERCISE 1
# My name is Sarah, so the first and last letter of my name (S + H = 19 + 8) give the number  27. The 27th Fibonacci number is 196,418.

# Forum Post EXERCISE 2
#My surname is Scholz
#
#The first letter S is number 83
#
#The last letter z is number 122
#
#Fibonacci number 205 is 3111581989804070186099320645726169127737705
#
#____
#
# ord() is a built-in function in Python. It is defined in the Python Standard Library: 
# "Given a string representing one Unicode character, return an integer representing the Unicode code point of that character. For example, ord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364. This is the inverse of chr()."
# For reference see: https://docs.python.org/3/library/functions.html#ord
