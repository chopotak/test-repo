from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

# Параметры подключения к PostgreSQL
db_params = {
    'database': 'dvdrental',
    'user': 'postgres',
    'password': 'admin',
    'host': 'localhost',  # Или адрес вашей PostgreSQL базы данных
    'port': '5432'  # Или порт вашей PostgreSQL базы данных
}

@app.route('/')
def index():
    # Устанавливаем соединение с базой данных
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Выполняем SQL-запрос для выборки данных из таблицы
    cursor.execute("SELECT * FROM film;")

    # Получаем результаты запроса
    data = cursor.fetchall()

    # Закрываем соединение с базой данных
    cursor.close()
    conn.close()

    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
