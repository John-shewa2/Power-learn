import pandas as pd

# Create a DataFrame with sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Grade': [60, 45, 80]
}
df = pd.DataFrame(data)
# Add a new column 'passed' where grade > 50 = True
df['passed'] = df['Grade'].apply(lambda x: True if x > 50 else False)
print("DataFrame with 'passed' column:\n", df)

# filter and display only students who passed
passed_students = df[df['passed']]
print("\nStudents who passed:")
print(passed_students)
