#WAP to input a number and display whether number is prime or not.

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Number is Prime")
else:
    print("Number is not Prime")
