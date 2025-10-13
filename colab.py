# Loading data
from google.colab import files
uploaded = files.upload()
# Data Preparation
import pandas as pd
auto_df = pd.read_csv('housing.csv.csv')
auto_df.head(7)
auto_df.info()
auto_df.describe()
auto_df.isnull().sum()
auto_df = auto_df.dropna()
auto_df.isnull().sum()
auto_df = auto_df.drop(columns=['ocean_proximity'])
auto_df.info()
# Missing values
missing_values = auto_df.isnull().sum()
print("Missing values per column:")
print(missing_values)
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
sns.heatmap(auto_df.isnull(), cbar=False, cmap='viridis')
plt.title('Heatmap of Missing Values')
plt.show()
# Data Analysis
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10, 6))
sns.heatmap(auto_df.corr(), annot=True, cmap='coolwarm')
plt.show()
# average sales per month and visualize monthly trends.Identify top-selling products or categories
plt.figure(figsize=(10, 6))
sns.histplot(auto_df['median_house_value'], bins=30, kde=True)
plt.title('Distribution of Median House Value')
plt.xlabel('Median House Value')
plt.ylabel('Frequency')
plt.show()
# Data Visualization
plt.figure(figsize=(10, 6))
sns.scatterplot(x='median_income', y='median_house_value', data=auto_df)
plt.title('Median Income vs Median House Value')
plt.xlabel('Median Income')
plt.ylabel('Median House Value')
plt.show()
# Correlation Analysis
correlation_matrix = auto_df.corr()
print(correlation_matrix['median_house_value'].sort_values(ascending=False))

# Splitting data
from sklearn.model_selection import train_test_split
X = auto_df.drop(columns=['median_house_value'])
y = auto_df['median_house_value']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Model Training
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
# Model Evaluation
from sklearn.metrics import mean_squared_error, r2_score
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')
# Save the model
import joblib
joblib.dump(model, 'linear_regression_model.pkl')
# Load the model
loaded_model = joblib.load('linear_regression_model.pkl')
# Make predictions with the loaded model
loaded_y_pred = loaded_model.predict(X_test)
print(f'Predictions from loaded model: {loaded_y_pred[:5]}')
# Upload the model file to Colab
files.download('linear_regression_model.pkl')
