#3. Operators
#1. Perform addition, subtraction, multiplication, and division.
a=10
b=38
print("a=",a)
print("b=",b)
print("Addition: ",a+b)
print("Substraction: ",a-b)
print("Multiplication: ",a*b)
print("Division: ",a/b)
print("---------------------------------")
#2. Find the remainder and quotient of two numbers.
num1=20
num2=67
print("remainder of 20 and 67: ",num1%num2)
print("quotient of 20 and 67: ",num1/num2)
print("---------------------------------")
#3. Check whether a number is even or odd.
n=int(input("Enter a number: "))
if n%2==0:
    print("Number is odd")
else:
    print("Number is even")

print("---------------------------------")
#4. Compare two numbers using relational operators.
n1=3432
n2=5656
print("3432 > 5656: ",n1 > n2)
print("3432 < 5656: ",n1 < n2)
print("3432 == 5656: ",n1 == n2)
print("3432 >= 5656: ",n1 >= n2)
print("3432 <= 5656: ",n1 <= n2)
print("3432 != 5656: ",n1 != n2)

#5. Demonstrate logical operators (and, or, not).
print("5>2 && 10>8",5>2 && 10>8)
print("12>90 || 39<9",12>90 || 39<9)
print("!(5>2)",!(5>2))
print("---------------------------------")
#6. Demonstrate assignment operators (+=, -=, *=, /=).
nn=50
print(nn)
print(nn+=10)
print(nn-=10)
print(nn*=4)
print(nn/=5)
print("---------------------------------")
#7. Find the largest of two numbers using comparison operators.
nn1=int(input("Enter number1: "))
nn2=int(input("Enter number2: "))
if nn1 > nn2:
    print(nn1," is largest")
else:
    print(nn2," is largest")
