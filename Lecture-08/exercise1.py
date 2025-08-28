def main():
    with open('employees.txt', 'r') as emp_file:    # เปิดไฟล์
        lines = emp_file.readlines()                # อ่านข้อมูลทั้งหมดมาเก็บใน list
    
    for i in range(0, len(lines), 3):
        name = lines[i].strip()
        emp_id = lines[i+1].strip()
        dept = lines[i+2].strip()                   # ลูปทีละ 3 บรรทัด (name, id, dept)

        
        print(f"Name: {name}")
        print(f"ID: {emp_id}")
        print(f"Dept: {dept}")                      # แสดงผลตามรูปแบบที่โจทย์ต้องการ
        print()                                     # เว้นบรรทัด

if __name__ == "__main__":
    main()