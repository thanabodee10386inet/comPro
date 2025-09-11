def divide (a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("CException: ", e)
    else:
        return result

a, b = map(int, input().split())
print(divide(a, b))
print("End of program") 