import pandas as pd

data = {'Namw': ['Alice', 'Bob', 'Charlie'],
         'Age': [25, 30, 35],
         'city': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

average_age = df['Age'].mean()
print("\nAverage Age:", average_age)

filtered_df = df[df['Age'] > 28]
print("\nFiltered DataFrame (Age > 28):\n", filtered_df)

df['Salary'] = [50000, 60000, 70000]
print("\nDataFrame with Salary column:\n", df)