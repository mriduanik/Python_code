import numbers
from unicodedata import name


name=['john','mosh','bob','rock']
print(name)
numbers=[2,3,5,67,64,78,997,2]
max=numbers[0]
for number in numbers:
    if number>max:
        max=number
print(max)
