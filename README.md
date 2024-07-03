# Tasks Overview

## Task 1 (Visualization of genders and age using Histogram)
This script visualizes the distribution of genders and ages in a population using bar charts and histograms with `matplotlib`.
Overview :
- **Bar Chart for Genders**: Displays the distribution of gender categories ('Male', 'Female', 'Other') using a bar chart.
- **Histogram for Ages**: Shows the distribution of ages in the population using a histogram with specified bins.
Usage :
Run the script to generate visual representations of the given gender and age data.
Requirements :
- `matplotlib` library for plotting the graphs.


## Task 2 (Titanic Dataset Analysis)
This script performs data cleaning and exploratory data analysis (EDA) on the Titanic dataset using `pandas`, `matplotlib`, and `seaborn`.
Overview :
- **Data Cleaning**: Handles missing values by dropping the 'Cabin' column, filling missing 'Age' values with the median age, and filling missing 'Embarked' values with the mode.
- **Exploratory Data Analysis**: 
  - Provides summary statistics of the dataset.
  - Visualizes survival rates by gender, passenger class, and embarkation point.
  - Analyzes age and fare distributions.
  - Displays a correlation heatmap of numerical features.
 Visualizations
- **Survival by Gender**: Count plot showing the number of survivors and non-survivors by gender.
- **Survival by Passenger Class**: Count plot showing the number of survivors and non-survivors by passenger class.
- **Age Distribution**: Histogram with a kernel density estimate (KDE) showing the distribution of ages.
- **Fare Distribution**: Histogram with a KDE showing the distribution of fares.
- **Survival by Embarkation Point**: Count plot showing the number of survivors and non-survivors by embarkation point.
- **Correlation Heatmap**: Heatmap displaying the correlations between numerical features.
Requirements
- `pandas` for data manipulation.
- `matplotlib` and `seaborn` for data visualization.
Usage
- Load the Titanic dataset as a CSV file named `titanic.csv`.
- Run the script to clean the data and generate visualizations.

