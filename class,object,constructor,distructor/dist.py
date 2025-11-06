class Student:
    def __init__(self):
        print("constructor is called now")
    
    def __del__(self):
        print("destructor is called now")
s1=Student()
