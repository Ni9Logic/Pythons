class Student:

    age = 0
    Class = "0"
    name = "0"

    def information(self):
        self.name = input("Enter your name: ")
        self.age = int(input('Enter your age: '))
        self.Class = input("Enter your class: ")
        print("--------------------------------")
        print("Name of the student is: ", self.name)
        print("Age of the student is: ", self.age)
        print("Class of the student is: ", self.Class)

def main():
    student1 = Student()
    print (student1.information())
    return 0