n=int(input("Enter the number"))
n1=n
b=0
while(n1>0):
   a=n1%10
   b=b*10+a
   n1=n1//10
if b==n:
    print "The number ",n,"is palindrome"
else:
     print "The number ",n,"is not palindrome"
     
