import os
from pymongo import MongoClient

# Подключение к базе данных
client = MongoClient('mongodb://localhost:27017/')

# Выбор базы данных
db = client['mydatabase']

# Выбор коллекции
users = db['users']

# Получение списка пользователей
user_list = users.find()

# Вывод списка пользователей
for user in user_list:
    print(user)

