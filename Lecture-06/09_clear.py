nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for sublist in nested_list: 
    sublist.clear()  #ลบรายการย่อยทั้งหมดใน nested_list
print(f"Cleared nested list: {nested_list}")  #ผลลัพธ์จะเป็น [[], [], []] เนื่องจากรายการย่อยทั้งหมดถูกลบออก