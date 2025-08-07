set1 = {1, 2, 3,}
set2 = {3, 4, 5}

# Union รวมสมาชิกของทั้งสองเซต
print(set1.union(set2)) # ส่งออกผล: {1, 2, 3, 4, 5}

# Intersection หาสมาชิกที่มีในทั้งสองเซต
print(set1.intersection(set2))  # ส่งออกผล: {3}

# Difference หาสมาชิกที่มีใน set1 แต่ไม่มีใน set2
print(set1.difference(set2))  # ส่งออกผล: {1, 2}

# Symmetric Difference หาสมาชิกที่มีใน set1 หรือ set2 แต่ไม่ทั้งสองเซต
print(set1.symmetric_difference(set2))  # ส่งออกผล: {1, 2, 4, 5}