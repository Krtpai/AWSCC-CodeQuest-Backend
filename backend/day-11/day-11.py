with open('names.txt', 'r') as file:
    names = file.readlines()

names.sort()

with open('names.txt', 'w') as file:
    file.writelines(names)