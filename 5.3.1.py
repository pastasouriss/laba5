import numpy as np
import matplotlib.pyplot as plt

a_values = np.arange(-5, 12.25, 1.75)
x_value = 12.1

f_values = np.exp(a_values * x_value) - 3.45 * a_values

for a, f in zip(a_values, f_values):
    print(f'a = {a}, f(a) = {f}')

max_value = np.max(f_values)
min_value = np.min(f_values)
average_value = np.mean(f_values)

print(f'\nМаксимальное значение: {max_value}')
print(f'Минимальное значение: {min_value}')
print(f'Среднее значение: {average_value}')
print(f'Количество элементов в массиве: {len(f_values)}')

sorted_f_values = np.sort(f_values)

plt.plot(a_values, f_values, marker='o', label='f(x)')
plt.axhline(y=average_value, color='r', linestyle='--', label='Среднее значение')
plt.xlabel('Значения a')
plt.ylabel('Значения f(x)')
plt.title('График функции f(x)')
plt.legend()
plt.grid(True)
plt.show()