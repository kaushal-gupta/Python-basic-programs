top=-1
stack=[]
def Push():
        item=int(input("\nEnter the item"))
        global top
        top=top+1
        stack.insert(top,item)
def Pop():
        if(len(stack)==0):
            print "Underflow"
        else:
             item=stack.pop()
             print "Item deleted is :",item
        
def display():
        if(len(stack)==0):
            print "Stack empty"
        else:
            print "[",
            for a in stack:
                print a," ",
            print "]"   
    

def peek():
        print len(stack)-1

    

while True:
 
    print "\nEnter 1: for push operation:"
    print "\nEnter 2: for pop operation:"
    print "\nEnter 3: for displaying the stack:"
    print "\nEnter 4: for peek"
    print "\nEnter 5: for Exit:"
    choice=int(input("Enter your choice:"))
    if(choice==1):
        Push()
    elif(choice==2):
        Pop()
    elif(choice==3):
        display()
    elif(choice==4):
        peek()
    elif(choice==5):
        break;
    else:
        print "Invalid choice"
        
        
