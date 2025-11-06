class Grandfather:
       def gardening(self):
              print("grandfather is gardening")
class Father(Grandfather):
       def driving(self):
              print("father is driving car")
class Child(Father):
       def study(self):
              print("child is studing")
c1=Child()
c1.gardening()
c1.driving()
c1.study()
