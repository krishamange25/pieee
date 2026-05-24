customer_id = "C001"
quantity = 5
price = 49.99

print(type(customer_id))
print(type(quantity))
print(type(price))

total = round(quantity * price, 2)
print(total)

print(int(price))
print(float(quantity))
print(int("100"))

'''
test cases 1
<class 'str'>
<class 'int'>
<class 'float'>

test cases 2
249.95
49
5.0
100

test cases 3
249.95

'''