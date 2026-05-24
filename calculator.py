num1 = float(input())
num2 = float(input())
op = input()

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    if num2 == 0:
        print("cannot divide by zero")
    else:
        print(num1 / num2)
else:
    print("invalid operator")
    
'''
test case 1 :
6
7
*

42.0

test case 2:
10
0
/


Cannot divide by zero!

test case 3:
10
5
+

15.0
'''