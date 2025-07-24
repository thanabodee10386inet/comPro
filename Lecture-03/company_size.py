employee = int(input("Enter the number of employee :  "))

if employee < 50:
    print("This is a small company.")
elif employee < 250:
    print("This is a medium-sized company.")
elif employee >= 250:
    print("Large Company")
