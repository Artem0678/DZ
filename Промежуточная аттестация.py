import pandas as pd

# Генерация DataFrame с одним столбцом
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Преобразование в one hot вид
unique_values = data['whoAmI'].unique()  # Получаем уникальные значения
one_hot_encoded = pd.DataFrame(0, columns=unique_values, index=range(len(data)))  # Создаем DataFrame для хранения результатов

for idx, value in enumerate(data['whoAmI']):
    one_hot_encoded.loc[idx, value] = 1  # Устанавливаем 1 для соответствующего столбца

# Объединение и вывод результатов
result = pd.concat([data, one_hot_encoded], axis=1)
result.drop('whoAmI', axis=1, inplace=True)  # Удаляем исходный столбец
result.head()
