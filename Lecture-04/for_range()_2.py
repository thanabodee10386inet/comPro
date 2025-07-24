num = int(input("Enter a number: "))
print("Number\tSquare")
print('--------------')

for number in range(1, 13):
    square = number * num
    print(number, '\t', square)