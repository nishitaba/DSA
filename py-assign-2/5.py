#5.	Write a function to check whether a number is even or odd.
def checkoddeven(num):
    if num % 2 == 0:
        print("Number:",num," is even")
    else:
        print("Number:",num," is odd")
checkoddeven(22)