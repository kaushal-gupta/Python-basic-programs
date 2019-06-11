n=int(input("Enter the number"))
n1=n
b=0
while(n1>0):
   a=n1%10
   b=b+a**3

   
   n1=n1//10
if b==n:
    print "The number ",n,"is armstrome"
else:
     print "The number ",n,"is not armstrome"
