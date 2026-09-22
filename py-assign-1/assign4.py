#4. Conditions

#1. Check whether a number is positive, negative, or zero.
n=int(input("Enter a number: "))
if n>0:
    print("Number is positive")
elif n<0:
    print("Number is negative")
else:
    print("Number is 0")
print("---------------------------------")
#2. Check whether a person is eligible to vote.
age=int(input("Enter your age: "))
if age>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")
print("---------------------------------")
#3. Find the largest of three numbers.
num1=int(input("Enter number1: "))
num2=int(input("Enter number2: "))
num3=int(input("Enter number3: "))
if num1>=num2 and num1>=num3:
    print(num1," is largest")
elif num2>=num1 and num2>=num3:
    print(num2," is largest")
else:
    print(num3," is largest")
print("---------------------------------")
#4. Check whether a year is a leap year.
year=int(input("Enter a year: "))
if year%4==0:
    print("Its a leap year")
else:
    print("Its not a leap year")
print("---------------------------------")    
#5. Create a grade system based on marks.
marks=float(input("Enter your marks: "))
if marks>=90:
    print("you obtained A grade")
elif marks>=80 and marks<90:
    print("you obtained B grade")
elif marks>=70 and marks<80:
    print("you obtained C grade")
elif marks>=60 and marks<70:
    print("you obtained D grade")
elif marks>=50 and marks<60:
    print("you obtained E grade")
else:
    print("you failed!")
print("---------------------------------")   
#6. Check whether a number is divisible by 5 and 11.
a=int(input("Enter a number: "))
if a%5==0 and a%11==0:
    print("number is divisible by 5 and 11")
else:
    print("number is not divisible by 5 and 11")
print("---------------------------------")
#7. Create a simple calculator using if-elif-else.
n1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
n2 = float(input("Enter the second number: "))

if operator == "+":
    result = n1 + n2
    print(f"Result: {n1} + {n2} = {result}")

elif operator == "-":
    result = n1 - n2
    print(f"Result: {n1} - {n2} = {result}")

elif operator == "*":
    result = n1 * n2
    print(f"Result: {n1} * {n2} = {result}")

elif operator == "/":

    if num2 != 0:
        result = n1 / n2
        print(f"Result: {n1} / {n2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")

else:
    print(f"Error: '{operator}' is not a valid operator.")
