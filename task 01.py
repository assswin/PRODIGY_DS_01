
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd



# Creating a DataFrame for categorical dat
data = pd.DataFrame({
    'Gender': ['Male', 'Female', 'Other'],
    'Count': [50, 45, 5]
})
# Creating a DataFrame for continuous data
ages = pd.Series([23, 25, 30, 30, 35, 40, 45, 50, 50, 55, 60, 65, 70])
# Create a bar chart
plt.figure(figsize=(8, 6))  # Set the figure size
sns.barplot(x='Gender', y='Count', data=data)

# Customize the chart
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Distribution of Gender')

# Show the plot
plt.show()
# Create a histogram
plt.figure(figsize=(8, 6))  # Set the figure size
plt.hist(ages, bins=5, edgecolor='black', color='skyblue')

# Customize the chart
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')

# Show the plot
plt.show()
