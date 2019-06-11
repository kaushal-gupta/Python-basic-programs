class ObjectPassing:
    def __init__(self):
        self.x=0
        self.y=0

    def update(self,x,y):
        self.x+=x
        self.y+=y

    def scope(self,ob1):
        self.x=ob1.x
        self.y=ob1.y

t1=ObjectPassing()
t2=ObjectPassing()
t1.update(15,26)
print "Before Passing t1",t1.x,t1.y
t3=t2.scope(t1)
print t3.x,t3.y
