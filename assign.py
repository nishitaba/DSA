#1)1. Create variables to store name, age, and city and display them.
name=input("Enter your Name: ")
age=int(input("Enter your age: "))
city=input("Enter your city: ")
print("Name: ",name,",Age: ",age,",City: ",city)
print("---------------------------------")
#2. Swap the values of two variables
a=10
b=20
print(a , b)
c=a
a=b
b=c
print(a , b)
print("---------------------------------")
#3. Calculate the area of a rectangle using variables.
length=int(input("Enter length: "))
breadth=int(input("Enter breadth: "))
print("Area of rectangle is: ",length*breadth)
print("---------------------------------")
#4. Calculate simple interest using variables.
p=int(input("Enter principal amount: "))
r=int(input("Enter interest rate: "))
t=int(input("Enter time period(in years): "))

si=(p*r*t)/100
print("Simple Interest: ",si)
print("---------------------------------")
#5. Convert Celsius temperature to Fahrenheit.
c=int(input("Enter celsius value: "))
f=(c * 9/5) + 32
print(c,"°C = ", f,"°F")


