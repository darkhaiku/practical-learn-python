import sys
sys.stdout = open('practical-learn-python', 'w')

import datetime
now = datetime.datetime.now()

#that str() has returned a human-readable date/time
print(str(now))
print('------')

#and repr() has returned a string that represents the Python code we would need to run to recreate this object.
print(repr(now))

sys.stdout.close()