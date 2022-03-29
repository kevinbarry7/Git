# January 5th 2019

import platform
import sys
print(platform.python_version())
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


print (sys.executable)
print(sys.version)

print("Hello World")
print(1 + 9)

message = "Hello Kevin"

test = message.replace('Kevin', 'April')
print(message)
print(len(message))
print(message[6])
print(message[-1])
print(message[0:5])
print(message.lower())
print(test)
print(test + ' ' + message)
message = '{}, {}. Welcome!'.format(message, test)
print(message)
message = f'{message}, {test}. Welcome!'
print(message)

name = "ada lovelace"
print(name.title())






