numbers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)