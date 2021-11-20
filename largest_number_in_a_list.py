numbers = [10, 20, 40, 60, 70, 80, 100]
largest_number = numbers[0]
for number in numbers:
    if number > largest_number:
        largest_number = number
print(largest_number)