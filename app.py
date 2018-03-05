import os
import time

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    print(f)
file = open("requirements.txt", 'w')
file.close()
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    print(f)