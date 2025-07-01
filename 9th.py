# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 15:53:22 2025
@author: gecw
"""

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets

# Load the Iris dataset
iris = datasets.load_iris()
print("Iris Data Set Loaded...")

# Split the dataset (10% test size)
x_train, x_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.1, random_state=0
)

# Display class labels
print("\nLabel mapping:")
for i, label in enumerate(iris.target_names):
    print(f"Label {i} -> {label}")

# Train the KNN model with k=2
classifier = KNeighborsClassifier(n_neighbors=2)
classifier.fit(x_train, y_train)

# Predict the test set
y_pred = classifier.predict(x_test)

# Print predictions vs actual labels
print("\nResults of Classification using K-NN with K=2:")
for i in range(len(x_test)):
    print(f"Sample {x_test[i]}, Actual Label: {iris.target_names[y_test[i]]}, Predicted Label: {iris.target_names[y_pred[i]]}")

# Accuracy
accuracy = classifier.score(x_test, y_test)
print(f"\nClassification Accuracy = {accuracy * 100:.2f}%")
