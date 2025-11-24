import pandas as pd

# Load the train.csv file
df = pd.read_csv('train.csv')

# Display the first 5 rows to confirm the data overview
print("First 5 rows of the dataset:")
print(df.head())

# Fill missing values in the 'Age' column with the overall median
median_age = df['Age'].median()
df['Age'] = df['Age'].fillna(median_age)

print("\nAfter filling missing values in the 'age' column:")
print(df.head())
