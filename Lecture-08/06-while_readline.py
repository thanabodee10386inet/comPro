with open("example.txt", "r") as file:
    line = file.readline()
    while line:
        print(line.strip())
        print("hello")
        line = file.readline()

# with open("example.txt", "r") as file:
#     line = file.readline()
#     while line:
#         print(line.strip())
#         line = file.readline()