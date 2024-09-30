import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0
std_dev = 1
num_samples = 1000

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Создание гистограммы
plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black')
plt.title('Гистограмма случайных данных')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.grid(axis='y', alpha=0.75)
plt.show()
