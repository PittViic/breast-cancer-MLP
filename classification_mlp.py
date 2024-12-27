# -*- coding: utf-8 -*-
"""classification-MLP

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1D9M3ArZyUGTUap0g2uEP3Nkt4g6MKfsU
"""

# Import necessary libraries
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

import seaborn as sns
import matplotlib.pyplot as plt

cancer_data = load_breast_cancer()
X, y = cancer_data.data, cancer_data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features by removing the mean and scal variance
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Creating a MLPClassifier Model
mlp = MLPClassifier(
    hidden_layer_sizes=(64, 32),
    max_iter=1000,
    random_state=42
)

# Training the model
mlp.fit(X_train, y_train)

# Make predictions on the test data
y_pred = mlp.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Generate a classification report
class_report = classification_report(y_test, y_pred)
print("Classification Report:\n", class_report)

# Gráfico de Curva

plt.figure(figsize=(8, 6))
plt.plot(mlp.loss_curve_, label="Loss Curve")
plt.title("Evolução da Função de Perda")
plt.xlabel("Iterações")
plt.ylabel("Perda")
plt.legend()
plt.grid(True)
plt.show

conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues")
plt.xlabel('Predito')
plt.ylabel('Real')
plt.title('Matriz de Confusão')
plt.show()