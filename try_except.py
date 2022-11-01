import sys
sys.stdout = open('practical-learn-python', 'w')

try:
    my_value = 3.14 / 0
except ArithmeticError:
    print('We had a general math error!')
except ZeroDivisionError:
    print('We had a divide-by-zero error')

sys.stdout.close()