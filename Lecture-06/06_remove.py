fruite_with_duplicates = ["apple", "banana", "apple", "cherry", "apple", "kiwi"]
while "apple" in fruite_with_duplicates:
    fruite_with_duplicates.remove("apple")  #ลบรายการ "apple" ออกจาก fruite_with_duplicates
print(f"fruits after remove: {fruite_with_duplicates}")  #ผลลัพธ์จะเป็น ["banana", "cherry", "kiwi"] เนื่องจาก "apple" ถูกลบออกทั้งหมด
