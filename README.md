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
    
- **Visualizations**:
- Survival by Gender: Count plot showing the number of survivors and non-survivors by gender.
- Survival by Passenger Class: Count plot showing the number of survivors and non-survivors by passenger class.
- Age Distribution: Histogram with a kernel density estimate (KDE) showing the distribution of ages.
- Fare Distribution: Histogram with a KDE showing the distribution of fares.
- Survival by Embarkation Point: Count plot showing the number of survivors and non-survivors by embarkation point.
- Correlation Heatmap: Heatmap displaying the correlations between numerical features.
  
Requirements
- `pandas` for data manipulation.
- `matplotlib` and `seaborn` for data visualization.
  
Usage
- Load the Titanic dataset as a CSV file named `titanic.csv`.
- Run the script to clean the data and generate visualizations.




## Task 3 (Bank Marketing Prediction)
This project uses a decision tree classifier to predict whether a client will subscribe to a term deposit based on the UCI Bank Marketing dataset.

Overview
- **Data Source**: [UCI Bank Marketing Dataset](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing)
- **Data Preprocessing**:
  - Categorical variables are encoded using one-hot encoding.
  - The target variable 'y' is converted from 'yes'/'no' to binary (1/0).

Steps
1. **Data Loading**: Load the dataset directly from the UCI repository.
2. **Encoding**: Apply one-hot encoding to categorical variables.
3. **Feature and Target Split**: Separate the data into features (X) and target (y).
4. **Train-Test Split**: Split the data into training and testing sets (80% train, 20% test).
5. **Model Training**: Train a decision tree classifier on the training data.
6. **Prediction**: Make predictions on the testing data.
7. **Evaluation**: 
   - Calculate accuracy of the model.
   - Generate a classification report with precision, recall, and F1-score.
8. **Visualization**: Plot the decision tree to visualize the model's decision-making process.

Results
- **Accuracy**: The accuracy of the decision tree classifier on the test data.
- **Classification Report**: Detailed performance metrics including precision, recall, and F1-score.

Requirements
- `pandas` for data manipulation.
- `scikit-learn` for machine learning and model evaluation.
- `matplotlib` for plotting the decision tree.

Usage
- Run the script to load the data, preprocess it, train the model, and evaluate its performance.
- Visualize the decision tree to understand the model's decisions.

