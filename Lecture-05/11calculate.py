def calculate_stats(numbers):
    totol_sum = sum(numbers)
    average = totol_sum / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return totol_sum, average, maximum, minimum

numbers = [5, 10, 15, 20, 25]
totol, avg, max_num, min_num = calculate_stats(numbers)

print(f"totol Sum: {totol}")
print(f"Average: {avg}")
print(f"maximum: {max_num}")
print(f"minimum: {min_num}")