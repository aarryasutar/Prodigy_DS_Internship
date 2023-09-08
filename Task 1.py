import matplotlib.pyplot as plt

# Example data for a categorical variable (e.g., genders in a population)
genders = ['Male', 'Female', 'Other']
gender_counts = [250, 300, 50]

# Example data for a continuous variable (e.g., ages in a population)
ages = [22, 28, 35, 42, 50, 65, 70, 80, 90, 95]
age_counts = [10, 20, 30, 40, 60, 80, 90, 50, 20, 5]

# Create a bar chart for the categorical variable (genders)
plt.bar(genders, gender_counts)
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Distribution of Genders in a Population')
plt.show()

# Create a histogram for the continuous variable (ages)
plt.hist(ages, bins=10, edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Distribution of Ages in a Population')
plt.show()
