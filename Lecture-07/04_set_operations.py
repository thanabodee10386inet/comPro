set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

untion_set =set1 | set2 # ส่งออกผล: {1, 2, 3, 4, 5, 6}
print("untion:", untion_set)  # รวมสมาชิกของทั้งสองเซต

intersection_set = set1 & set2  # ส่งออกผล: {3, 4}
print("intersection:", intersection_set)  # หาสมาชิกที่มีในทั้งสองเซต

difference_set = set1 - set2  # ส่งออกผล: {1, 2}
print("difference:", difference_set)  # หาสมาชิกที่มีใน set1 แต่ไม่มีใน set2

sym_diff_set = set1 ^ set2  # ส่งออกผล: {1, 2, 5, 6}
print("symmetric difference:", sym_diff_set)  # หาสมาชิกที่มีใน set1 หรือ set2 แต่ไม่ทั้งสองเซต
# ส่งออกผล: {1, 2, 5, 6}