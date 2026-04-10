'''write a python program to input marks of 4 subjects and display total,percentage,result and grade.
if student is fail (<40) in any subject then result should be displayed ass "FAIL" and grade shoould be
displayed as "With Held**".'''

Name=input("Enter Your Name:")
University=input("Enter Your University Name:")
Dept=input("Enter Your Dept Name:")
sub1= int(input("Enter marks of subject 1 :"))
sub2= int(input("Enter marks of subject 2 :"))
sub3= int(input("Enter marks of subject 3 :"))
sub4= int(input("Enter marks of subject 4 :"))

total= sub1+sub2+sub3+sub4
per= total/4

if sub1<40 or sub2<40 or sub3<40 or sub4<40:
    print("Total is : ",total)
    print("Percentage is :",per)
    print("Result is : FAIL")
    print("Grade is : With Held**")

elif per>90:
    print("Total is : ",total)
    print("Percentage is :",per)
    print("Result is : PASS")
    print("Grade is : A+")
    
elif per in range(80,91):
    print("Total is : ",total)
    print("Percentage is :",per)
    print("Result is : PASS")
    print("Grade is : A")

elif per in range(70,81):
    print("Total is : ",total)
    print("Percentage is :",per)
    print("Result is : PASS")
    print("Grade is : B+")

elif per in range(60,71):
    print("Total is : ",total)
    print("Percentage is :",per)
    print("Result is : PASS")
    print("Grade is : B")

elif per in range(50,61):
    print("Total is : ",total)
    print("Percentage is :",per)
    print("Result is : PASS")
    print("Grade is : C")

elif per in range(40,51):
    print("Total is : ",total)
    print("Percentage is :",per)
    print("Result is : PASS")
    print("Grade is : D")

else:
    print("Invalid input")
