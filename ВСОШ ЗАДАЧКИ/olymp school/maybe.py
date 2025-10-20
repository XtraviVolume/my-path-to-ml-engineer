import pandas as pd
import os  # <-- 1. Добавь этот импорт

# 2. Эта магия находит полный путь к папке, где лежит твой скрипт
script_dir = os.path.dirname(os.path.abspath(__file__))

# 3. Это имя твоего файла
file_name_only = 'data.csv' 

# 4. Это "склеивает" путь к папке и имя файла, получая полный путь
file_name = os.path.join(script_dir, file_name_only)

# 5. Теперь pandas будет искать файл по полному, точному пути
df = pd.read_csv(file_name, header=None)

# --- Дальше твой код без изменений ---
x = df.iloc[:, 2]

x_bar = x.mean()

is_outlier = (x - x_bar).abs() > x_bar

outlier_count = is_outlier.sum()

print(outlier_count)