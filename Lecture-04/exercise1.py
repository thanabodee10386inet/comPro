print('KPH\tMPH')
print('-----------------')

for KPH in range(50, 131, 10):
    MPH = KPH * 0.6214
    print(f"{KPH}\t{MPH:.1f}")