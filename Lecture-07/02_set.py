fruits = {'apple', 'banana', 'cherry'} # สร้างชุดข้อมูลผลไม้

fruits.add('orange')  # เพิ่ม 'orange' ลงในชุดข้อมูล
print(fruits)  # ส่งออกผล: {'banana', 'cherry', 'apple', 'orange'}

fruits.remove('banana')  # ลบ 'banana' ออกจากชุดข้อมูล
print(fruits)  # ส่งออกผล: {'cherry', 'apple', 'orange'}

fruits.discard('grape')  # ลบ 'grape' ถ้ามีอยู่ในชุดข้อมูล (ไม่เกิดข้อผิดพลาดถ้าไม่มี)
print(fruits)  # ส่งออกผล: {'cherry', 'apple', 'orange'}

remove_item = fruits.pop()  # ลบสมาชิกแรกที่ถูกเพิ่ม (ไม่รับประกันลำดับ)
print(remove_item) # ส่งออกผล: 'cherry' หรือ 'apple' หรือ 'orange'
print(fruits)  # ส่งออกผล: {'apple', 'orange'} หรือ {'cherry', 'orange'} หรือ {'cherry', 'apple'}

fruits.clear()  # ล้างชุดข้อมูลทั้งหมด
print(fruits)  # ส่งออกผล: set() (ชุดข้อมูลว่างเปล่า)