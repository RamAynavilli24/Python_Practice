
class Student:
    college_name = "ABC College"
    departments = ["Arts","Economics","Science"]

    def __init__(self,name,roll,dept):
        self.name = name
        self.roll = roll
        self.dept = dept

    def study(self, n_hours):
        print(f"The student studies for {n_hours} per day")

    def sports(self, sport_name):
        print(f"The student plays {sport_name}")

    @classmethod
    def greet(cls):
        print(cls)
        print(f"Welcome to the {cls.college_name}")


student1 = Student("Naresh",1001,"Science")
print(student1.__module__)
print(student1.college_name)
print(student1.departments)
student1.study(5)
student1.greet()

