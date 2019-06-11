def Lsearch(L,i,n):
    count=0
    for a in L:
        count+=1
        if(a==i):
            return 0
        elif(count==n):
            return 1
        
        


n=int(input("Enter the size of the list"))
print " Enter the elments for the list"
lit=[0]*n

for i in range(0,n):
    lit[i]=int(input("enter the element"+str(i)+":"))

item=int(input("Enter the Element You want to search"))
c=Lsearch(lit,item,n)
if(c==0):
    print "The element found"
elif(c==1):
    print 'the element not found'
