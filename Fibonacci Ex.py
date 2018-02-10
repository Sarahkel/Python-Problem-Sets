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

name = "scholz"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
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
#ord()
#returns the Unicode code point for a one-character string