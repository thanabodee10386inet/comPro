with open('sales.txt', 'r') as sales_file:
    total_sales = 0.0
    for line in sales_file:
        amount = float(line.strip())
        total_sales += amount
        print(f"Sales amount: {amount, '.2f'}")
print(f"total sales: {total_sales, '.2f'}")

# with open('sales.txt', 'r') as sales_file:
#     for line in sales_file:
#         amount = float(line)
#         print(format(amount, '.2f'))