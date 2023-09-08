import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic dataset
titanic_data = pd.read_csv('titanic.csv')

# Data Cleaning
# Handle missing values
titanic_data.drop(['Cabin'], axis=1, inplace=True)  # Drop the 'Cabin' column due to too many missing values
titanic_data['Age'].fillna(titanic_data['Age'].median(), inplace=True)  # Fill missing age values with the median age
titanic_data['Embarked'].fillna(titanic_data['Embarked'].mode()[0], inplace=True)  # Fill missing 'Embarked' values with mode

# EDA
# Explore the data with summary statistics
print(titanic_data.describe())

# Visualize the data
# Survival by gender
sns.set_style('whitegrid')
sns.countplot(x='Survived', hue='Sex', data=titanic_data, palette='RdBu_r')
plt.title('Survival by Gender')
plt.show()

# Survival by passenger class
sns.countplot(x='Survived', hue='Pclass', data=titanic_data, palette='viridis')
plt.title('Survival by Passenger Class')
plt.show()

# Age distribution
sns.histplot(titanic_data['Age'].dropna(), kde=True, bins=30)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# Fare distribution
sns.histplot(titanic_data['Fare'], kde=True, bins=30)
plt.title('Fare Distribution')
plt.xlabel('Fare')
plt.ylabel('Count')
plt.show()

# Survival by embarkation point
sns.countplot(x='Survived', hue='Embarked', data=titanic_data, palette='Set2')
plt.title('Survival by Embarkation Point')
plt.show()

# Correlation heatmap
corr_matrix = titanic_data.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Heatmap')
plt.show()
