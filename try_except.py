import sys
sys.stdout = open('practical-learn-python', 'w')

try:
    int('a')
except ValueError as error:
    print(f"something went wrong. Message: {error}")

print('Reached end of the program.')

sys.stdout.close()