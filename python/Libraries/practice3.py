import matplotlib.pyplot as plt
# create a bar chart that shows 5 countries and their populations
countries = ['USA', 'China', 'India', 'Brazil', 'Nigeria']
populations = [331002651, 1439323776, 1380004385, 212559417, 206139589]

plt.bar(countries, populations, color='skyblue')
plt.title("Population of Countries")
plt.xlabel("Countries")
plt.ylabel("Population")
plt.show()

# create a pie chart that shows how a student spends their time in 24 hours
labels = ['Sleep', 'Study', 'Leisure', 'Exercise', 'Meals']
sizes = [8, 6, 5, 2, 3]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Student's Daily Activities")
plt.show()

# a line chart that shows temperature changes during the day (morning, noon, evening, night).
times = ['Morning', 'Noon', 'Evening', 'Night']
temperatures = [20, 25, 22, 18]
plt.plot(times, temperatures, marker='o', color='orange')
plt.title("Temperature Changes Throughout the Day")
plt.xlabel("Time of Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
