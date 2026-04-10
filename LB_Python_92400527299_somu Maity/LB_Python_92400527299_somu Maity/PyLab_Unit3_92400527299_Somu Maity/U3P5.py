#Write a program to print factorial number using function.

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
n= int(input("Enter the number:"))
print("The factorial of ", n ,"is " ,factorial(n))
