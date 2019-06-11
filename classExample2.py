class Student:
     nos=0
     def __init__(self,rno,name,mks):
         self.rollno=rno
         self.name=name
         self.marks=mks
         self.grade=""
         Student.nos+=1


     def clacgrade(self): 

         if self.marks>90:
             self.grade="A"
         elif self.marks>70:
            self.grade="B"
         else:
             self.grade="C"


stud1=Student(1,'sumit',90)
stud2=Student(3,'rahul',60)
stud1.clacgrade()
stud2.clacgrade()
print stud1.__dict__
print Student.__name__
print Student.__module__
print Student.__bases__
print Student.__doc__
