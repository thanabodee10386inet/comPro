survey_results = [
    ["Python", "JavaScript", "C++"],
    ["Python", "JavaScript", "C#"],
    ["Python", "Java"],
    ["Python", "C++" ,"JavaScript"],
    ["Python", "JavaScript", "C++", "Java"],
]  # Example survey results


choice_sets = [set(i) for i in survey_results] # ใช้ set comprehension เพื่อสร้างชุดข้อมูลจากผลสำรวจ
common_languages = set.intersection(*choice_sets) # หาภาษาที่ถูกเลือกโดยผู้เข้าร่วมทุกคน
print("Languages chosen by all participants:", common_languages) # แสดงผลภาษาที่ถูกเลือกโดยผู้เข้าร่วมทุกคน

only = set.union(*choice_sets) - choice_sets[0] - choice_sets[-1] # หาภาษาที่ถูกเลือกโดยผู้เข้าร่วมเพียงคนเดียว
print("Languages only chosen by one participant:", only) # แสดงผลภาษาที่ถูกเลือกโดยผู้เข้าร่วมเพียงคนเดียว

unique_languages = set.union(*choice_sets) # หาภาษาที่ถูกเลือกโดยผู้เข้าร่วมทั้งหมด
print("Number of unique languages:", len(unique_languages))  # แสดงผลจำนวนภาษาที่ถูกเลือกโดยผู้เข้าร่วมทั้งหมด

two = set.union(*choice_sets) - choice_sets[0] & choice_sets[-1] # หาภาษาที่ถูกเลือกโดยผู้เข้าร่วมสองคน
print("Languages chosen by exactly two participants:", two) # แสดงผลภาษาที่ถูกเลือกโดยผู้เข้าร่วมสองคน