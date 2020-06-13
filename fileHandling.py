import json
from dateutil import parser

# file handling
# 1) without using with statement
file = open('file_WOstatement', 'w')
file.write('hello world ! La serie de guatemala se llama Jose?')
file.close()

# 2) without using with statement
file = open('file_WOstatementtry', 'w')
try:
    file.write('hello world')
finally:
    file.close()

# using with statement
with open('file_Statement', 'w') as file:
    file.write('hello world using with statement!')

with open('activities.json', 'w') as json_file:
    json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])