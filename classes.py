class Car:
    """
    This is the car class of multiple brands for the demo
    """
    def color(self):
        print("Green")

obj1 = Car()
obj2 = Car()

obj1.color()

print(obj1.color)
print(type(obj2))
print(Car.__doc__)