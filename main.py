import pandas as pd

# Чтение данных из CSV файла
df = pd.read_csv('dz.csv')

# Вывод информации о DataFrame
print(df.info())

# Группировка по городу и вычисление среднего значения зарплаты
sz = df.groupby('City')['Salary'].mean()

# Вывод среднего значения зарплаты по городам
print(sz)