import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv("expanded_traffic_safety_data.csv")

# Setting up the general styling for seaborn
sns.set(style="whitegrid")

# Bar Graph 1: Total Accidents by City
plt.figure(figsize=(8, 5))
accidents_by_city = data.groupby('City')['Accidents'].sum()
accidents_by_city.plot(kind='bar', color='skyblue')
plt.title('Total Accidents by City')
plt.xlabel('City')
plt.ylabel('Total Accidents')
plt.show()

# Pie Chart 1: Accidents by Weather Condition
plt.figure(figsize=(7, 7))
accidents_by_weather = data.groupby('Weather')['Accidents'].sum()
accidents_by_weather.plot(kind='pie', autopct='%1.1f%%', startangle=140, cmap="Pastel1")
plt.title('Accidents by Weather Condition')
plt.ylabel('')  # Clean up for pie chart
plt.show()

# Bar Graph 2: Average Traffic Volume by Day
plt.figure(figsize=(10, 6))
avg_traffic_by_day = data.groupby('Day')['Traffic Volume'].mean().reindex(
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
avg_traffic_by_day.plot(kind='bar', color='coral')
plt.title('Average Traffic Volume by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Average Traffic Volume')
plt.show()

# Pie Chart 2: Accidents by Day of the Week
plt.figure(figsize=(7, 7))
accidents_by_day = data['Day'].value_counts()
accidents_by_day.plot(kind='pie', autopct='%1.1f%%', startangle=140, cmap="tab10")
plt.title('Accidents Distribution by Day of the Week')
plt.ylabel('')
plt.show()

# Scatter Plot: Traffic Volume vs. Accidents
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Traffic Volume', y='Accidents', hue='Weather', data=data, palette='deep')
plt.title('Traffic Volume vs. Accidents (Colored by Weather)')
plt.xlabel('Traffic Volume')
plt.ylabel('Accidents')
plt.legend(title='Weather')
plt.show()

# Box Plot: Accidents by Weather Condition
plt.figure(figsize=(10, 6))
sns.boxplot(x='Weather', y='Accidents', data=data, palette='Set2')
plt.title('Distribution of Accidents by Weather Condition')
plt.xlabel('Weather Condition')
plt.ylabel('Accidents')
plt.show()
