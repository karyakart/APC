class Car:
    def carname(self):
        print("honda city")
class Bike():
    def bikename(self):
        print("yamaha Fz250")
class Auto(Car,Bike):
    def vehicalname(self):
        print("bajaj three wheeler")


c1=Auto()
c1.vehicalname()
c1.bikename()
c1.carname()