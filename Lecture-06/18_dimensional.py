import random

ROWS = 3  # จำนวนแถว
COLS = 4  # จำนวนคอลัมน์

def main():

    values = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    
    for r in range(ROWS):  # วนลูปตามจำนวนแถว
        for c in range(COLS):
            values[r][c] = random.randint(1, 100) # กำหนดค่าแบบสุ่มในช่วง 1 ถึง 100

    print(values)  # แสดงผลลัพธ์ของ matrix

main()
