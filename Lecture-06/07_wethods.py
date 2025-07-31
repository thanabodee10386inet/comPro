grades = [85, 90, 78, 92, 88]
third_grade = grades.pop(2)  #ลบและคืนค่ารายการที่ตำแหน่ง 2
grades.append(third_grade)  #เพิ่ม third_grade กลับไปที่ท้ายรายการ
print(f"Grades after pop: {grades}")  #ผลลัพธ์จะเป็น [85, 90, 92, 88, 78] เนื่องจาก 78 ถูกลบออกและเพิ่มกลับไปที่ท้ายรายการ