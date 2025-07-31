animals = ["cat", "dog", "rabbit", "hamster", "dog", "parrot"]  # รายการสัตว์ที่มีการทำซ้ำ
first_dog_index = animals.index("dog")  # ค้นหาตำแหน่งแรกของ "dog"
print(f"The first dog is at index: {first_dog_index}")  # แสดงตำแหน่งของ "dog" ในรายการ

second_dog_index = animals.index("dog", first_dog_index + 1)  # ค้นหาตำแหน่งที่สองของ "dog" โดยเริ่มค้นหาจากตำแหน่งถัดไป
print(f"The second dog is at index: {second_dog_index}")  # แสดงตำแหน่งของ "dog" ที่สองในรายการ
