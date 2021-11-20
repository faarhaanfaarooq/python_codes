names = ["Jhon", "Sara", "Mosh", "Don", "Striver"]
            # 0       1       2       3       4
            # -5     -4      -3      -2      -1
# To print all the elements of a list serially
for name in names:
    print(name)
print('*******************************')
# Indecis of the elements in the list
print(names[-1], names[1])
print('*******************************')
# For showing elements specifically
print(names[2:4])
print(names[2:])
print('*******************************')
# For changing an element in the list
names[0] = "Laura"
print(names[0])
