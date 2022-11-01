import sys
sys.stdout = open('practical-learn-python', 'w')

try:
    int('a')
except ValueError:
    print("Oops, couldn't convert that value into an int!")

print('Reached end of the program.')

sys.stdout.close()