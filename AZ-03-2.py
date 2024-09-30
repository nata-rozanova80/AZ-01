import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
x = np.random.rand(5)  # массив из 5 случайных чисел для оси X
y = np.random.rand(5)  # массив из 5 случайных чисел для оси Y

# Построение диаграммы рассеяния
plt.scatter(x, y, color='red')
plt.title('Диаграмма рассеяния')
plt.xlabel('Случайные данные X')
plt.ylabel('Случайные данные Y')
plt.grid()
plt.show()
