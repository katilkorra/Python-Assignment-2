# 

import sys

# Open the file in read mode
with open('hello.txt', 'r') as input_file:
    text = input_file.read()

# Replace all occurrences of 'Lorem' with 'POOJA'
if (text.find("Gujarat") != -1) :
    text = text.replace('Gujarat', 'GUJRAT')
    print(text)
else:
    print("not found")







