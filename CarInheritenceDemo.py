class Vehicle:
    company = "Duke Motors"
    def __init__(self,wheels,seats,millage):
        print("Init of Vehicle")
        self.wheels = wheels
        self.seats = seats
        self.millage = millage

    def get_details(self):
        print(f"This vehicle has {self.wheels} wheels, {self.seats} seats and gives {self.millage}KM millage per one liter. ")

v1 = Vehicle(4,5,20)

v1.get_details()

class Car(Vehicle):
    model = "XYZ Model"

    def __init__(self,car_type,drive_type):
        print("Init of Car")
        self.car_type = car_type
        self.drive_type = drive_type
        Vehicle.__init__(self,4,7,18)
#  Or you can call like super().__init__(4,5,19)
        #super().__init__(4,5,19)

c1 = Car("SUV","Automatic")
print(c1.model)
print(c1.company)
print(c1.millage)


