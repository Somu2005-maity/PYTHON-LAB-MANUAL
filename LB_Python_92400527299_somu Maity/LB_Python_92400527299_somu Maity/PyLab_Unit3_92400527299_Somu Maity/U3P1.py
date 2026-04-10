'''WAP to input a number and display factorial of that number.
For example, Factorial of 5 = 5 * 4 * 3 * 2 * 1 = 120.'''

'''def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
n= int(input("Enter the number:"))
print("The factorial of ", n ,"is :" ,factorial(n))'''

n=int(input("Enter Number:"))

f = 1
for i in range(1,n+1):
    f=f*i
print(f)
