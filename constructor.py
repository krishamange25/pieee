class Student:

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(self.name)
        print(self.age)
        print(self.marks)

    def grade(self):
        if self.marks >= 70:
            print("A")
        elif self.marks >= 50:
            print("B")
        else:
            print("C")

name = input()
age = input()
marks = input()

if name == "" or age == "" or marks == "":
    print("input cannot be blank")
else:
    try:
        age = int(age)
        marks = int(marks)
        s = Student(name, age, marks)
        s.display()
        s.grade()
    except ValueError:
        print("invalid input")

'''
test case 1:-
Input:
Ankit
21
75

Output:
Ankit
21
75
A

test case 2:-
Input:

Output:
input cannot be blank

test case 3:-
Input:
Raj
abc
xyz

Output:
invalid input
'''