def greet():
    print("hello welcome")

def add(a, b):
    print(a + b)

def student(name, age=18):
    print(name)
    print(age)

def multiply(a, b):
    return a * b

greet()

a = input()
b = input()
name = input()
age = input()

if a == "" or b == "" or name == "" or age == "":
    print("input cannot be blank")
else:
    a = int(a)
    b = int(b)
    age = int(age)
    
    add(a, b)
    student(name, age)
    result = multiply(a, b)
    print(result)

'''
test case 1 :
hello welcome

test case 2:
Input:

Expected Output:
input cannot be blank

test case 3:
Input:
6
7
19

Expected Output:
hello welcome
13
19
42
'''