#1 using object reference

#class studentdata():
#    clg="NRI Academy"
#    def __init__(self,name,rollno,age,section):
#        self.name=name
#        self.rollno=rollno
#        self.age=age
#        self.section=section
#    def progress(self):
#        print(self.clg,self.name,self.rollno,self.age,self.section)
#a=studentdata("saiteja",41,25,"A")
#a.progress()
#studentdata("akhil",42,25,"A").progress()
#print()


#2 using class reference

#class studentdata():
#    clg="NRI Academy"
#    def __init__(self,name,rollno,age,section):
#        self.name=name
#        self.rollno=rollno
#        self.age=age
#        self.section=section
#    def progress(self):
#        print(studentdata.clg,self.name,self.rollno,self.age,self.section)
#a=studentdata("SAITEJA",41,25,"A")
#a.progress()
#studentdata("AKHIL",42,25,"A").progress()
#print()

#class studentdata():
#    clg="NRI Academy"
#    def record(self,name,rollno,age,section):
#        self.name=name
#        self.rollno=rollno
#        self.age=age
#        self.section=section
#    def progress(self):
#        print(self.clg,self.name,self.rollno,self.age,self.section)
#a=studentdata("SAITEJA",41,25,"A")
#a.record
#a.progress()   #type error'''


#3 using only normal method

#class studentdata():
#    clg="NRI academy"
#    def record(self):
#        name="saiteja"
#        age=25
#        rollno=41
#        section="A"
#        print(studentdata.clg,name,rollno,age,section)
#a=studentdata()
#a.record()
#print()

#4 using only constructor

#class studentdata():
#    clg="NRI academy"
#    def __init__(self,name,rollno,age,section):
#        self.name=name
#        self.rollno=rollno
#        self.age=age
#        self.section=section
#        print(self.clg,self.name,self.rollno,self.age,self.section)
        
#a=studentdata("saiteja",41,25,"A")
#b=studentdata("akhil",42,25,"A")
#c=studentdata("vishu",43,25,"A")
#d=studentdata("abhi",44,26,"A")
#e=studentdata("naresh",45,25,"A")
#print()


#5 using 2 normal methods

#class studentdata():
#    clg="NRI ACEDAMY"
#    def record(self):
#        name="saiteja"
#        age=25
#        rollno=41
#        section="A"
#        print(studentdata.clg,name,rollno,age,section)
#    def progress(self):
#        name="akhil"
#        age=25
#        rollno=42
#        section="A"
#        print(studentdata.clg,name,rollno,age,section)
#a=studentdata()
#a.record()
#a.progress()
#print()

#static variable print statement outside the method

class studentdata():
    clg="NRI acedamy"
    def record(self):
        name="saiteja"
        age=25
        rollno=41
        section="A"
        print("hi")
    print(studentdata.clg)
a=studentdata()
a.record()
print() 