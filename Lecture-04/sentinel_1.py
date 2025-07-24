rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

i = 0
while i < rows:
    j = 0
    while j < columns:
        print("*", end=" ")
        j += 1
    print()
    i += 1