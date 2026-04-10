p=int(input("Enter principal amount:"))
r=int(input("Enter rate of interest:"))
n=int(input("Enter number of years:"))

si=p*r*n/100
i=p+si

print("Simple Interest is ",si)
print("Payable amount is",i)
