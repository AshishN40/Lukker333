"""Practical on basic programs using python for introducing and using python environment such as, 
a)	Program to print multiplication table for given no. 
Sol:
"""
num = int(input("Display multiplication table of? "))

for i in range(1, 11):
  print(num, 'x', i, '=', num * i)
'''b)Program to check whether the given no is prime or  not.
Sol:'''
num = int(input("Enter a number: "))

if num == 1:
  print(num, "is not a prime number")
elif num > 1:

  for i in range(2, num):
    if (num % i) == 0:
      print(num, "is not a prime number")

      break
  else:
    print(num, "is a prime number")

else:
  print(num, "is not a prime number")


"""c) Program to find factorial of the given no and similar programs.
Sol:"""
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
  print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
  print("The factorial of 0 is 1")
else:
  for i in range(1, num + 1):
    factorial = factorial * i
print("The factorial of", num, "is", factorial)
