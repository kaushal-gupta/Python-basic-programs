
class Stack:

    def __init__(self):
        self.stack=list()
    def Push(self):
        item=int(input("\nEnter the item"))
        self.stack.append(item)


    def Pop(self):
        if(len(self.stack)==0):
            print "Underflow"
        else:
             item=self.stack.pop()
             print "Item deleted is :",item
        
    def display(self):
        if(len(self.stack)==0):
            print "Stack empty"
        else:
            print "[",
            for a in self.stack:
                print a," ",
            print "]"   
    

    def peek(self):
        print len(self.stack)

    
bj=Stack()
while True:
 
    print "\nEnter 1: for push operation:"
    print "\nEnter 2: for pop operation:"
    print "\nEnter 3: for displaying the stack:"
    print "\nEnter 4: for peek"
    print "\nEnter 5: for Exit:"
    choice=int(input("Enter your choice:"))
    if(choice==1):
        bj.Push()
    elif(choice==2):
        bj.Pop()
    elif(choice==3):
        bj.display()
    elif(choice==4):
        bj.peek()
    elif(choice==5):
        break;
    else:
        print "Invalid choice"
        
        




