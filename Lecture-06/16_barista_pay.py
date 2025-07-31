NUM_EMPLOYEES = 6

def main():
    hours = [0] * NUM_EMPLOYEES  # สร้างรายการ hours ที่มีค่าเริ่มต้นเป็น 0 สำหรับพนักงานแต่ละคน

    for index in range(NUM_EMPLOYEES): # วนลูปเพื่อรับข้อมูลชั่วโมงทำงานของพนักงานแต่ละคน
        print('Enter the hours worked by employee', \
              index + 1, ': ', sep='', end='')  # แสดงข้อความเพื่อขอข้อมูลชั่วโมงทำงาน
        hours[index] = float(input())  # รับข้อมูลชั่วโมงทำงานจากผู้ใช้และเก็บไว้ในรายการ hours

        pay_rate = float(input('Enter the pay rate for employee: '))    # รับข้อมูลอัตราค่าจ้างต่อชั่วโมงของพนักงาน

        for index in range(NUM_EMPLOYEES): # วนลูปเพื่อคำนวณและแสดงผลค่าจ้างรวมของพนักงานแต่ละคน
            gross_pay = hours[index] * pay_rate # คำนวณค่าจ้างรวมโดยการคูณชั่วโมงทำงานกับอัตราค่าจ้าง  
            print('Grooss pay for employee', index + 1, ': $', \
                  format(gross_pay, ',.2f'), sep='')    # แสดงผลค่าจ้างรวมของพนักงานแต่ละคนในรูปแบบที่มีจุดทศนิยม 2 ตำแหน่ง

main()