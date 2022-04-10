def find_max(numbers):
    max=numbers[0]
    for number in numbers:
        if number>max:
            max=number
    return max


print(find_max([2,4,5,7]))
