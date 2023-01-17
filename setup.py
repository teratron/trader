import os

with open('.env') as handle:
    lines = handle.readlines()

try:
    for line in lines:
        ind = line.find('=')
        key = line[:ind].strip(" ")
        os.environ[key] = line[ind + 1:].strip(" ")
        print(ind, key, os.environ[key])
except ValueError:
    pass

SECRET = os.environ['TERMINAL_PATH']
print(SECRET)
