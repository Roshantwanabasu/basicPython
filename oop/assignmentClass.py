from __future__ import print_function
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

car1 = Vehicle()
car1.name = "Fer"
car1.color = "red convertible"
car1.value = 60000.00
car2 = Vehicle()
car2.name = "Jump"
car2.color = "Blue"
car2.kind = "Van"
car2.value = 10000.00

customVehicle = Vehicle()
customVehicle.name = input("Enter the name of your vehicle:")
customVehicle.kind = input("Enter what kind of vehicle it is:")
customVehicle.color = input("Enter color of  vehicle:")
customVehicle.value = float(input("Enter the price of the vehicle:"))
print(car1.description())
print(car2.description())
print(customVehicle.description())