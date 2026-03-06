def add(P,Q):
    #this is used for adding 2 numbers 
    return P+Q
def subtract(P,Q):
    #this is used for subtracting 2 numbers
    return P - Q
def multiply(P,Q): 
    #this is used for multiplying 2 numbers
    return P*Q
def divide(P,Q):
    #this is used for dividing 2 numbers 
    return P/Q

#now take inputs from the user 
print('please select the opreation:')
print('a,Add')
print('b,Subtract')
print('c,multiply')
print('d,divide')
choice = input('please enter choice(a/ b/ c/ d):')

num_1 = int(input('enter number 1:'))
num_2 = int(input('enter second number:'))

if choice == 'a':
    print(num_1,'+',num_2,'=',add(num_1,num_2))
elif choice == 'b':
    print(num_1 ,'-',num_2,'=',subtract(num_1,num_2))
elif choice == 'c':
    print(num_1,'*',num_2,'=',multiply(num_1,num_2))
elif choice == 'd':
    print(num_1,'/',num_2,'=',divide(num_1,num_2))
else:
    print('this is an invalid input')