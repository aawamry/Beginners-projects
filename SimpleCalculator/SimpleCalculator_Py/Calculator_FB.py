def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print('please choose operation: \n'
              '1 - Addition \n'
              '2 - Subtraction \n'
              '3 - Multiplication \n'
              '4 - Division \n')

select = int(input('Please Select an Operator: '))
num1 = int(input('Please Enter Number1: '))
num2 = int(input('Please Enter Number2: '))





if select == 1:
    print(num1, '+', num2, '=', add(num1, num2))
elif select == 2: 
    print(num1, '-', num2, '=', subtract(num1, num2))
elif select == 3:
    print(num1, '*', num2, '=', multiply(num1, num2))
elif select == 4:
    print(num1, '/', num2, '=', divide(num1, num2))
else:
    print('Please Enter a Valid Number')










