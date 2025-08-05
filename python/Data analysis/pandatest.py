import pandas as pd

# Creating DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago'],
        'gender': ['F', 'M', 'M']
        }

df = pd.DataFrame(data)
df['Country'] = ['USA', 'USA', 'USA']  # Adding a new column
df_filtered = df[df['Age'] < 28]  # Filtering rows where Age is less than 28
# Sorting by Age in descending order
df_sorted = df.sort_values(by='Age', ascending=False)
print(df)
print(df_filtered)
print(df_sorted)
