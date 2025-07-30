import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

# A numpy array of numbers from 1 to 10 and their mean
numbers = np.arange(1, 11)
mean_value = np.mean(numbers)

# A pandas DataFrame and display summary statistics
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 6, 7, 8, 9],
    'C': [9, 10, 11, 12, 13]
}
df = pd.DataFrame(data)
print(df.describe())

# Fetch data from a public API using requests and print a key piece of information
response = requests.get('https://api.github.com')
if response.status_code == 200:
    api_data = response.json()
    print(f"API Status: {api_data['current_user_url']}")

# plot a simple line graph using matplotlib
plt.plot(numbers, numbers**2)
plt.title('Numbers vs. Squares')
plt.xlabel('Numbers')
plt.ylabel('Squares')
plt.show()
