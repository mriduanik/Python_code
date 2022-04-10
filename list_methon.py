from list import*


numbers=[2,4,4,5,7,8,9]
numbers.append(20)
print(numbers)
numbers.insert(0, 10)
print(numbers)
numbers.remove(8)
print(numbers)
print(numbers.index(4))
numbers.sort()
print(numbers)
numbers2=numbers.copy()