''' 
Data Visualization III
Download the Iris flower dataset or any other dataset into a DataFrame. (e.g.,
https://archive.ics.uci.edu/ml/datasets/Iris ). Scan the dataset and give the inference as:
1. List down the features and their types (e.g., numeric, nominal) available in the dataset.
2. Create a histogram for each feature in the dataset to illustrate the feature distributions. 
3. Create a boxplot for each feature in the dataset. 
4. Compare distributions and identify outliers. 

'''


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Load the dataset
iris = pd.read_csv("iris.csv")

# 1. List features and their types
print("Dataset Features:")
print(iris.dtypes)

# 2. Histograms for each feature
iris.hist(figsize=(10, 6), bins=20, edgecolor='black')
plt.suptitle("Feature Distributions - Histograms")
plt.show()

# 3. Boxplots for each feature
plt.figure(figsize=(12, 8))
num_features = len(iris.columns[:-1]) 
for i, col in enumerate(iris.columns[1:-1]): 
    plt.subplot((num_features - 1) // 2 + 1, 2, i + 1)  
    sns.boxplot(y=iris[col])
    plt.title(f"Boxplot of {col}")
plt.tight_layout()
plt.show()

# 4. Outlier detection using IQR
print("Outliers (IQR Method):")
for col in iris.columns[:-1]:
    Q1 = iris[col].quantile(0.25)
    Q3 = iris[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = iris[(iris[col] < lower_bound) | (iris[col] > upper_bound)]
    print(f"{col}: {len(outliers)} outliers")
    print(outliers)
    plt.subplot((num_features - 1) // 2 + 1, 2, i + 1)
    sns.boxplot(y=iris[col])
    sns.stripplot(y=outliers[col], color='red', jitter=True, label='Outliers')
    plt.title(f"Outliers in {col}")
plt.tight_layout()
plt.show()

# 5. Outlier detection using Z-score
print("Outliers (Z-score Method):")
z_scores = stats.zscore(iris.iloc[:, :-1])
outliers_z = (abs(z_scores) > 3).any(axis=1)
outliers_data = iris[outliers_z]
print(outliers_data)

plt.figure(figsize=(10, 6))
for i, col in enumerate(iris.columns[:-1]):
    plt.subplot((num_features - 1) // 2 + 1, 2, i + 1)
    sns.boxplot(y=iris[col])
    sns.stripplot(y=outliers_data[col], color='blue', jitter=True, label='Outliers')
    plt.title(f"Z-score Outliers in {col}")
plt.tight_layout()
plt.show()
