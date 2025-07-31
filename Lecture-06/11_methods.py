heroes = ['Ironman', 'Thor', 'Hulk', 'Superman', 'Spiderman']
h2 = ['Dr. Strangs', 'Cpt. America', 'Black panther', 'Ant Man']

heroes.insert(0, h2[0]) # แทรก Dr. Strangs ที่ตำแหน่ง 0
print(heroes.index('Thor')) # แสดงตำแหน่งของ Thor
heroes.insert(heroes.index('Thor'), h2[1]) # แทรก Cpt. America หลัง Thor
print(heroes)  # แสดงรายการ heroes หลังจากแทรก Cpt. America
heroes.remove('Spiderman')  # ลบ Spiderman ออกจาก heroes
heroes.append('Ant Man')  # เพิ่ม Antman ที่ท้ายรายการ heroes
print(heroes) # แสดงรายการ heroes หลังจากการลบและเพิ่ม
heroes.sort()  # เรียงลำดับ heroes ตามตัวอักษร
print(heroes)
heroes.reverse()  # กลับรายการ heroes
print(heroes)  # แสดงรายการ heroes หลังจากกลับรายการ
newheroes = heroes # สร้างสำเนาของ heroes
newheroes[0] = 'Wonder Woman' # แก้ไขชื่อแรกใน newheroes
print(heroes) # แสดง heroes หลังจากแก้ไขชื่อใน newheroes
copyheroes = [] + heroes  # สร้างสำเนาของ heroes
print(copyheroes)  # แสดงสำเนาของ heroes
copyheroes[0] = 'Hanuman' # แก้ไขชื่อแรกใน copyheroes
print(heroes)  # แสดง heroes หลังจากแก้ไขชื่อ
print(copyheroes)  # แสดง copyheroes หลังจากแก้ไขชื่อ
