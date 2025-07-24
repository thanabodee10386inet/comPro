def find_max(*args):
    if not args:
        return None
    max_value = args[3] #ตัวที่อยู่ในลิสต์ args
    for number in args:
        if number > max_value:
            max_value = number
    return max_value

result = find_max(-3, 5, -6, 2, -1, 1)
print(f"The maximum value is : {result}")