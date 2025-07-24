hour = int(input("Enter a hour: "))
pay = int(input("pay rate: "))

if hour > 40:
    gross_pay = ((hour - 40) *1.5*pay) + (40 * pay)
else :
    gross_pay = (hour * pay)

print("Gross Pay : " ,gross_pay)


'''gross_pay = (hour*pay)
print('gross pay is : ' ,gross_pay)'''