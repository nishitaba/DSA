#10.	Write a function to check whether a number is positive, negative, or zero.
def num_check(a):
   if a > 0:
       print(a," is positive")
   elif a < 0:
       print(a," is negative")
   else:
       print("num is 0")
num_check(0)