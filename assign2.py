#2. Data Types
#1. Demonstrate int, float, str, bool, and complex.
a=10
b=2.5
c="Hello"
d=True
e=10+7j
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print("---------------------------------")
#2. Accept two numbers and display their data types.
num1=int(input("Enter an integer: "))
num2=float(input("Enter a float value: "))
print(num1, type(num1))
print(num2, type(num2))
print("---------------------------------")
#3. Convert a string number into an integer and float.
s1=12
f1=float(s1)
print(s1)
print(f1)
print("---------------------------------")
#4. Find the length of a string.
word="Hello from python"
print("Length of String '",word,"' is ",len(word))
print("---------------------------------")
#5. Create a list, tuple, set, and dictionary and display their types.
l1=[1,2,3,4,5]
t1=(10,20,30,40,50)
s1={100,200,300,400,500}
d1={1:'a',2:'b',3:'c',4:'d',5:'e'}
print(l1 , type(l1))
print(t1 , type(t1))
print(s1 , type(s1))
print(d1 , type(d1))
