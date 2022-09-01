import pymysql

from config import host, user, password, db_name
from mysql.connector import connect, Error

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")

    try:
        # Создал базу данных
        # with connection.cursor() as cursor:
        #     create_base = "CREATE DATABASE venus;"
        #     cursor.execute(create_base)
        #     print("create_database")

        # Просмотреть все базы данных
        # with connection.cursor() as cursor:
        #     show_db_query = "SHOW DATABASES;"
        #     cursor.execute(show_db_query)
        #     for db in cursor:
        #         print(db)

        # Создал таблицу "automobile"
        # with connection.cursor() as cursor:
        #     create_table_automobile = "CREATE TABLE `automobile`(id int AUTO_INCREMENT PRIMARY KEY," \
        #                          " title VARCHAR(100)," \
        #                          " release_year YEAR(4)," \
        #                          " car_body_type VARCHAR(100)," \
        #                          " price_$ DECIMAL(6,1));"
        #     cursor.execute(create_table_automobile)
        #     connection.commit()
        #     print("Table created successfully")

        # Запрос на получение имен всех таблиц в базе данных
        # with connection.cursor() as cursor:
        #     table_name = "SHOW TABLES;"
        #     cursor.execute(table_name)
        #     for tab in cursor:
        #         print(tab)

        # Создал таблицу "auto_critic"
        # with connection.cursor() as cursor:
        #     create_table_auto_critic = "CREATE TABLE `auto_critic`(id int AUTO_INCREMENT PRIMARY KEY," \
        #                          " first_name VARCHAR(100)," \
        #                          " last_name VARCHAR(100));"
        #     cursor.execute(create_table_auto_critic)
        #     connection.commit()
        #     print("Table created successfully")

        # Создал таблицу "ratings"
        # with connection.cursor() as cursor:
        #     create_table_ratings = "CREATE TABLE ratings" \
        #                          "(automobile_id INT," \
        #                          " auto_critic_id INT," \
        #                          " rating DECIMAL(2,1)," \
        #                          " FOREIGN KEY(automobile_id) REFERENCES automobile(id)," \
        #                          " FOREIGN KEY(auto_critic_id) REFERENCES auto_critic(id)," \
        #                          " PRIMARY KEY(automobile_id, auto_critic_id));"
        #     cursor.execute(create_table_ratings)
        #     connection.commit()
        #     print("Table created successfully")

        # Получил информацию о столбцах в таблице 'automobile'
        # with connection.cursor() as cursor:
        #     show_table = "DESCRIBE automobile;"
        #     cursor.execute(show_table)
        #     result = cursor.fetchall()
        #     for res in result:
        #         print(res)

        # Изменил схему таблицы
        # with connection.cursor() as cursor:
        #     alter_table = "ALTER TABLE automobile MODIFY COLUMN price_$ INT;"
        #     show_table = "DESCRIBE automobile;"
        #     cursor.execute(alter_table)
        #     cursor.execute(show_table)
        #     result = cursor.fetchall()
        #     print("Схема таблицы automobile после изменения:")
        #     for res in result:
        #         print(res)

        # Удаление таблицы
        # with connection.cursor() as cursor:
        #     drop_table = "DROP TABLE ratings;"
        #     cursor.execute(drop_table)

        # Вставка записей с помощью .execute()
        # with connection.cursor() as cursor:
        #     insert_automobile = "INSERT INTO automobile (title, release_year, car_body_type, price_$)" \
        #                         "VALUES" \
        #                         "('Honda Civic X', 2016, 'sedan', 26000),"\
        #                         "('Opel Astra K', 2018, 'universal', 15500),"\
        #                         "('Mercedes-Benz C', 2019, 'universal', 27700),"\
        #                         "('Porsche Cayenne', 2013, 'suv', 30000),"\
        #                         "('Bentley Continental', 2014, 'coupe', 76500);"
        #     cursor.execute(insert_automobile)
        #     connection.commit()
        #     print("Данные добавлены")

        # Вставка записей с помощью .executemany()
        # with connection.cursor() as cursor:
        #     insert_auto_critic = "INSERT INTO auto_critic (first_name, last_name) VALUES ( %s, %s )"
        #     auto_critic_records = [
        #         ('Marina', 'Gerasimova'),
        #         ('Vika', 'Alfirovich'),
        #         ('Vasya', 'Zuenok'),
        #         ('Vadim', 'Yakjik')
        #     ]
        #     cursor.executemany(insert_auto_critic, auto_critic_records)
        #     connection.commit()
        #     print("Данные добавлены")

        # Вставка записей с помощью.executemany()
        # with connection.cursor() as cursor:
        #     insert_ratings = "INSERT INTO ratings (rating, automobile_id, auto_critic_id) VALUES ( %s, %s, %s)"
        #     ratings_records = [
        #         (7.5, 3, 4), (9.0, 1, 1), (8.5, 2, 1), (5.3, 3, 2),
        #         (6.4, 5, 3), (8.1, 5, 4), (7.7, 4, 4), (6.3, 2, 2),
        #         (9.8, 1, 4)
        #     ]
        #     cursor.executemany(insert_ratings, ratings_records)
        #     connection.commit()
        #     print("Данные добавлены")

        # Чтение записей с ограничением кол-ва строк
        # with connection.cursor() as cursor:
        #     select_auto_critic = "SELECT * FROM auto_critic LIMIT 3;"
        #     cursor.execute(select_auto_critic)
        #     result = cursor.fetchall()
        #     for row in result:
        #         print(row)

        # Чтение записей со смещением на 2стр, и ограничением в 3стр
        # with connection.cursor() as cursor:
        #     select_automobile = "SELECT title, release_year FROM automobile LIMIT 2, 3;"
        #     cursor.execute(select_automobile)
        #     for row in cursor.fetchall():
        #         print(row)

        # Фильтрация автомобилей со стоимостью более 27000, ORDER BY от самой высокой цены, до самой низкой
        # with connection.cursor() as cursor:
        #     select_automobile = "SELECT title, price_$ FROM automobile WHERE price_$ > 27000 ORDER BY price_$ DESC;"
        #     cursor.execute(select_automobile)
        #     for auto in cursor.fetchall():
        #         print(auto)

        # CONCAT для объединения строк, получаем 3 самые дорогие авто вместе с датами их выпуска
        # with connection.cursor() as cursor:
        #     select_automobile = "SELECT CONCAT(title, ' (', release_year, ')')," \
        #                         " price_$ FROM automobile ORDER BY price_$ DESC LIMIT 3;"
        #     cursor.execute(select_automobile)
        #     for auto in cursor.fetchall():
        #         print(auto)

        # Тоже самое, только с использованием .fetchmany(), для очистки оставшихся рез. доп. использ. cursor.fetchall()
        # with connection.cursor() as cursor:
        #     select_automobile = "SELECT CONCAT(title, ' (', release_year, ')'), " \
        #                         "price_$ FROM automobile ORDER BY price_$ DESC;"
        #     cursor.execute(select_automobile)
        #     for auto in cursor.fetchmany(size=3):
        #         print(auto)
        #     cursor.fetchall()

        # Обработка нескольких таблиц JOIN, узнаем 3 авто с самым высоким рейтингом
        # with connection.cursor() as cursor:
        #     select_automobile_ratings = "SELECT title, AVG(rating) as average_rating FROM ratings " \
        #                                 "INNER JOIN automobile ON automobile.id = ratings.automobile_id " \
        #                                 "GROUP BY automobile_id ORDER BY average_rating DESC LIMIT 3;"
        #     cursor.execute(select_automobile_ratings)
        #     for auto_rat in cursor.fetchall():
        #         print(auto_rat)

        # Имя авто-критика, давшего наибольшее количество оценок
        # with connection.cursor() as cursor:
        #     select_auto_critic = "SELECT CONCAT(first_name, ' ', last_name), " \
        #                          "COUNT(*) as num FROM auto_critic INNER JOIN ratings " \
        #                          "ON auto_critic.id = ratings.auto_critic_id GROUP BY " \
        #                          "auto_critic_id ORDER BY num DESC LIMIT 1;"
        #     cursor.execute(select_auto_critic)
        #     for crit in cursor.fetchall():
        #         print(crit)

        # Обновление записей, сменил фамилию у Вики
        # with connection.cursor() as cursor:
        #     update_auto_critic = "UPDATE auto_critic SET last_name = 'Cooper' " \
        #                          "WHERE first_name = 'Vika';"
        #     cursor.execute(update_auto_critic)
        #     connection.commit()
        #     print('Данные изменены')

        # Удалить все оценки определенного авто-критика, но для начала убедиться, что удаляю нужные записи
        with connection.cursor() as cursor:
            select_automobile = "SELECT auto_critic_id, automobile_id FROM ratings WHERE auto_critic_id = 3"
            cursor.execute(select_automobile)
            for auto in cursor.fetchall():
                print(auto)
        #     delete_ratings = "DELETE FROM ratings WHERE auto_critic_id = 3"
        #     cursor.execute(delete_ratings)
        #     connection.commit()
        #     print('Записи удалены')

    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)

# Скрипт, который позволяет корректировать оценки
# automobile_id = input("Enter automobile id: ")
# auto_critic_id = input("Enter auto_critic id: ")
# new_rating = input("Enter new rating: ")
# update_rating = "UPDATE ratings SET rating = %s " \
#                "WHERE automobile_id = %s AND auto_critic_id = %s; " \
#                "SELECT * FROM ratings WHERE automobile_id = %s AND auto_critic_id = %s"
# val_tuple = (
#     new_rating,
#     automobile_id,
#     auto_critic_id,
#     automobile_id,
#     auto_critic_id,
# )
# try:
#     with connect(
#         host="localhost",
#         user=user,
#         password=password,
#         database=db_name,
#     ) as connection:
#         with connection.cursor() as cursor:
#             for result in cursor.execute(update_rating, val_tuple, multi=True):
#                 if result.with_rows:
#                     print(result.fetchall())
#             connection.commit()
# except Error as e:
#     print(e)