class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)
        print(self.age)

class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def display(self):
        super().display()
        print(self.marks)

try:
    name = input()
    age = int(input())
    marks = int(input())
    Student(name, age, marks).display()
except ValueError:
    print("invalid input")

'''
test case 1:
Input:
Raj
20
85

Output:
Raj
20
85

test case 2:
Input:
Raj
abc
xyz

Output:
invalid input

test case 3:
Input:

Output:
invalid input
'''