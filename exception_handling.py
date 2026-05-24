try:
    num1 = int(input())
    num2 = int(input())
    result = num1 / num2
    print(result)

except ValueError:
    print("error please enter numbers only")

except ZeroDivisionError:
    print("error cannot divide by zero")

except Exception as e:
    print("something went wrong:", e)

finally:
    print("program finished")
    
'''
Test Case 1 

Input: 
10
2
Output:
5.0
program finished

Test Case 2 

Input:
10  
0
Output:
error cannot divide by zero
program finished

Test Case 3 

Input: 
abc
Output:
error please enter numbers only
program  finished
'''