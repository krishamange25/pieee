stack = []

try:
    n = int(input())

    for i in range(n):
        choice = int(input())

        if choice == 1:
            value = int(input())
            stack.append(value)

        elif choice == 2:
            if len(stack) > 0:
                stack.pop()

    print(stack)

    if len(stack) > 0:
        print(stack[-1])
    else:
        print("stack is empty")

except:
    print("invalid input")

'''
test case 1:
Input:
4
1
10
1
20
1
30
2

Output:
[10, 20]
20

test case 2:
Input:
2
2
2

Output:
[]
stack is empty

test case 3:
Input:
abc

Output:
invalid input
'''