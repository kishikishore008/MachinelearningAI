from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load dataset (Example with Iris dataset)
iris = load_iris()
X = iris.data
y = iris.target

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Gaussian Naive Bayes Classifier
clf_nb = GaussianNB()

# Train the classifier
clf_nb.fit(X_train, y_train)

# Predict on the test set
predictions_nb = clf_nb.predict(X_test)

# Calculate accuracy
accuracy_nb = accuracy_score(y_test, predictions_nb)
print(f"Naïve Bayes Classifier Accuracy: {accuracy_nb}")
