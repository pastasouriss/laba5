import numpy as np
import random
X = np.column_stack([np.ones(12), np.random.randint(9, 22, size=12), np.random.randint(60, 83, size=12)])
Y = np.random.uniform(13.5, 18.6, size=12)
A = np.linalg.inv(X.T @ X) @ (X.T @ Y)
Y_pred = X @ A
print("Оценки уравнения регрессии (A):")
print(A)
print("\nПроверка результатов:")
print("Исходный вектор Y:")
print(Y)
print("\nПредсказанный вектор Y:")
print(Y_pred)