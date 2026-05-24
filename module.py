import math

num1 = input()
num2 = input()

if num1 == "" or num2 == "":
    print("input cannot be blank")
else:
    try:
        num1 = float(num1)
        num2 = float(num2)
        print(math.sqrt(num1))
        print(math.ceil(num2))
        print(math.floor(num2))
    except ValueError:
        print("invalid input")

'''
**TC1 — Valid Input**
Input: 25 / 4.7
Output:
5.0
5
4

**TC2 — Blank Input**

Input: 
(blank)
Output: 
input cannot be blank


**TC3 — Invalid Input**

Input: 
abc
Output: 
invalid input
'''