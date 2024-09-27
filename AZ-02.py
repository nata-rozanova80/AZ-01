import pandas as pd

# Чтение данных из CSV файла
df = pd.read_csv('Students.csv')

# Вывод информации о DataFrame
print(df.head())

# Создаем словарь для хранения средних оценок
average_scores = {}
median_scores = {}
scores = {}
so = {}

# Перебираем все столбцы в DataFrame
for column in df.columns:
    # Проверяем, является ли столбец числовым и не является ли он '№' или 'Имя ученика'
    if pd.api.types.is_numeric_dtype(df[column]) and column not in ['№', 'Имя ученика']:
        # Вычисляем среднее значение и добавляем в словарь
        average_scores[column] = df[column].mean()
        median_scores[column] = df[column].median()
        so[column] = df[column].std()
        
scores[column] = {'mean': average_scores, 'median': median_scores, 'std': so}

# Выводим средние оценки
for subject in average_scores.keys():
    average = average_scores[subject]
    medians = median_scores[subject]
    stds = so[subject]
    print(f'Предмет: {subject}')
    print(f'Средняя оценка по {subject}: {average}')
    print(f'Медианная оценка по {subject}: {medians}')
    print(f'Стандартное отклонение по {subject}: {stds}')

#Вычислите Q1 и Q3 для оценок по математике:

Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR = Q3_math - Q1_math

print('')
print(f'Q1 по математике - {Q1_math}')
print(f'Q3 по математике - {Q3_math}')
print(f'IQR по математике - {IQR}')