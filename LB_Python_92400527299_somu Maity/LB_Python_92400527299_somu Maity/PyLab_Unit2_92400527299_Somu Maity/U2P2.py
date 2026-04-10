#wap to input age of person and display message as follows.
'''if age < 12 print you are kid
-if age between 12 to 17 print you are teenager
-if age between 18 to 60 print you are adult
-if age > 60 print you are senior citizen'''

age=int(input("Enter the age:"))

if age<12:
    print("You Are Kid")
elif age in range(12, 18):
    print("You Are teenager")
elif age in range(18, 61):
    print("You Are Adult")
else:
    print("You Are Senior Citizen")
