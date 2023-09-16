import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load the dataset
data = pd.read_csv('a.csv')

# Display the first few rows of the dataset
print(data.head())

# Separate features and target
X = data.drop(['name', 'status'], axis=1)
y = data['status']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train a Random Forest classifier
classifier = RandomForestClassifier(random_state=42)
classifier.fit(X_train, y_train)

# Predict the target values on the test set
y_pred = classifier.predict(X_test)

# Print classification report
print(classification_report(y_test, y_pred))

# Visualize feature importances
feature_importances = pd.Series(classifier.feature_importances_, index=X.columns)
feature_importances.nlargest(10).plot(kind='barh')
plt.show()
