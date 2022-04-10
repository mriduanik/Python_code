
numbers=[2,3,4,5,6,7,7]
unique=[]
for number in numbers:
    if number not in numbers:
        unique.append(number)
print(unique)
print(numbers)