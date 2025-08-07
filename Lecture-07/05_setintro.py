setA = {1, 2, 3, 4}
setB = set([8, 9, 10])

setA.add(5)             # เพิ่มสมาชิก 5 ลงใน setA
setB.update([6, 7])     # เพิ่มสมาชิก 6 และ 7 ลงใน setB
Uset = setA | setB      # รวมสมาชิกของ setA และ setB
print(Uset)             # ส่งออกผล: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(len(Uset))        # ส่งออกผล: 10

setB.update('ABCD')     # เพิ่มสมาชิก A, B, C, D ลงใน setB
setA.update([6, 7, 8])  # เพิ่มสมาชิก 6, 7, 8 ลงใน setA
print(setB)             # ส่งออกผล: {6, 7, 8, 9, 10, 'A', 'B', 'C', 'D'}

print(setA.intersection(setB))  # ส่งออกผล: {6, 7, 8} (สมาชิกที่มีในทั้งสองเซต)
print(setA ^ setB)      # ส่งออกผล: {1, 2, 3, 4, 5, 9, 10, 'A', 'B', 'C', 'D'} (สมาชิกที่มีใน setA หรือ setB แต่ไม่ทั้งสองเซต

setB.remove('B')        # ลบสมาชิก 'B' ออกจาก setB
setB.discard('10')      # ลบสมาชิก '10' ถ้ามีอยู่ใน setB (ไม่เกิดข้อผิดพลาดถ้าไม่มี)
print(setB)             # ส่งออกผล: {6, 7, 8, 9, 'A', 'C', 'D'}
print(setA.clear())     # ล้างสมาชิกทั้งหมดใน setA
for val in Uset:
    print(val)          # แสดงสมาชิกทั้งหมดใน Uset
