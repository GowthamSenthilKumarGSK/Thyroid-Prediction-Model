import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("D:/Project/predictive_final_dataset.csv")

# Remove rows with non-numeric values in the 'age' column
df = df[df['age'].apply(lambda x: str(x).isdigit())]

# Set the aesthetic parameters for all plots
sns.set(rc={'figure.figsize': [8, 8]}, font_scale=1.2)

# Create a distribution plot for the 'age' column
sns.distplot(df['age'].astype(float))
plt.show()

# Create a count plot for the 'sex' column
sns.countplot(x='sex', data=df)
plt.show()

# Create a joint plot for 'TSH' and 'binaryClass'
sns.jointplot(x='TSH', y='binaryClass', data=df, kind='scatter', height=8, color='m')
plt.show()

# Create a joint plot for 'TT4' and 'binaryClass'
sns.jointplot(x='age', y='TT4', data=df, kind='scatter', height=8, color='m')
plt.show()

# Create a strip plot for 'binaryClass' and 'age'
sns.stripplot(x="binaryClass", y="age", data=df, palette="viridis")
plt.show()