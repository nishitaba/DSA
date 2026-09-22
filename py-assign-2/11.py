#11.	Write a function to find the maximum of three numbers.
def max_num(a,b,c):
    if a > b and a > c:
        print(a," is max")
    elif b>a and b>c:
        print(b," is max")
    else:
        print(c," is max")
max_num(1,4,30)