def add(a,b):
    return a + b
def subtract(a,b):
    return a - b 
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == '0':
        raise SyntaxError
    return a/b

print('what do you want to do')
print('you can g - add , s - subtract , m - multiply , d - divide')
choice = input('enter your choice of operation')
choice.lower
num_1 = float(input('enter a number'))
num_2 = float(input('enter a number'))
if choice == g:
    result = a + b
    print(result)
elif choice == s:
    result = a - b
    print(result)
elif choice == m:
    result = a*b
    print('result')
elif choice == d:
    result = a/b
    print(result)
else:
    print("invalid output")




    