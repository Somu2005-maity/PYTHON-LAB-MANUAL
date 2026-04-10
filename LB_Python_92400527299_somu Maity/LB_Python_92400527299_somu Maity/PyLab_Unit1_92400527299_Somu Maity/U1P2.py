a= int(input("Enter the first number:"))
b= int(input("Enter the second number:"))
c= input("Enter the arithmetic operator(+,-,*,/):")

if c=='+':
    print("Addition is :", a+b)
elif c=='-':
    print("Subtraction is :", a-b)
elif c=='*':
    print("Multiplication is :", a*b)
elif c=='/':
    print("Division is :", a/b)
elif c=='%':
    print("Modulus is :", a%b)
else:
    print("Invalid Operator")

