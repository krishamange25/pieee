import threading
import time

def task1():
    print("thread 1 is running")
    time.sleep(1)
    print("thread 1 is completed")

def task2():
    print("thread 2 is running")
    time.sleep(1)
    print("thread 2 is completed")

try:
    choice = int(input())

    if choice == 1:
        t1 = threading.Thread(target=task1)
        t2 = threading.Thread(target=task2)

        t1.start()
        t2.start()

        t1.join()
        print("thread 1 is waiting for thread 2")

        t2.join()
        print("both threads completed")

    elif choice == 2:
        t1 = threading.Thread(target=task1)
        t2 = threading.Thread(target=task2)

        t1.start()
        t2.start()

    else:
        print("invalid input")

except:
    print("invalid input")

'''
test case 1:
Input:
1

Output:
Thread 1 is running
Thread 2 is running
Thread 1 is completed
Thread 1 is waiting for Thread 2
Thread 2 is completed
Both threads completed


test case 2:
Input:
2

Output:
Thread 2 is running
Thread 1 is running
Thread 1 is completed
Thread 2 is completed


test case 3: 
Input:
5

Output:
Invalid input
'''