p=int(input("Enter principal amount:"))
r=int(input("Enter rate of interest:"))
n=int(input("Enter number of years:"))

si=p*r*n/100
ci=p*(1+r/100)**n-p
i=p+si

print("Simple Interest is ",si)
print("Compound Interest is ",ci)
print("Payable amount is",i)
