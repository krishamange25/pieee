queue = []

try:
    n = int(input())

    for i in range(n):
        choice = int(input())

        if choice == 1:
            value = int(input())
            queue.append(value)

        elif choice == 2:
            if len(queue) > 0:
                queue.pop(0)

    print(queue)

    if len(queue) > 0:
        print(queue[0])
    else:
        print("queue is empty")

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
[20, 30]
20

test case 2:
Input:
2
2
2

Output:
[]
queue is empty


test case 3 :
Input:
abc

Output:
invalid input
'''