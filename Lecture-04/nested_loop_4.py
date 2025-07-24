num_str = int(input("Enter a number: "))

if num_str > 100:
    print("ห้ามเกิน100จ่ะ")

for num in range(num_str, 101):
    print(f"{num} {num}")

