#syntax of class

class Animal: #class declaration
    def display(self):
        print("animals make sound!")
    
a1=Animal() #object creation
a1.display()

class Student:
    def disp(self,name,age):
        self.name=name
        self.age=age
        print(self.name)
        print(self.age)
    
s1=Student()
s1.disp("prathamesh",20)