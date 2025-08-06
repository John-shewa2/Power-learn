# Load the CSV file using pandas.
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('E:\Power learn\python\Data analysis\sales_data.csv')
print(df)

# Calculate total revenue
total_revenue = df['Revenue'].sum()
print(f'Total Revenue: {total_revenue}')

# Find the best-selling product (based on Quantity Sold).
best_selling_product = df.loc[df['Quantity sold'].idxmax()]
print(f"Best Selling Product: {best_selling_product['Product']}")

# Identify the day with the highest sales.
highest_sales_day = df.loc[df['Revenue'].idxmax()]
print(f"Highest Sales Day: {highest_sales_day['Date']}")

# Save the results to a new file called sales_summary.txt
with open('E:\Power learn\python\Data analysis\sales_summary.txt', 'w') as f:
    f.write(f'Total Revenue: {total_revenue}\n')
    f.write(f'Best Selling Product: {best_selling_product["Product"]}\n')
    f.write(f'Highest Sales Day: {highest_sales_day["Date"]}\n')

# Visualize sales trends using matplotlib

plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Revenue'], marker='o')
plt.title('Sales Revenue Over Time')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()
