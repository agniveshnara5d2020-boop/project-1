try:
    age = int(input('age:'))
    if age <= 0:
        print('ERROR,age must be greater thn 0')
    elif age>120:
        print('age entered is unrealistic')
    else:
        print('age is valid')

        if age%2==0:
            print('age is even')
        else:
            print('age is odd')
except ValueError:
    print('ERROR:enter a valid number')
