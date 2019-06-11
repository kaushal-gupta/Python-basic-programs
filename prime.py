a=int(input("Enter the number"))
for i in range(2,a):
    if a%i==0:
        break;
if i==a-1:
    print "prime"
else:
    print "not prime"

