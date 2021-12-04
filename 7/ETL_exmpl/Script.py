import sqlite3
import pandas as pd

# from datetime import datetime, timedelta
import httplib2

from oauth2client.service_account import ServiceAccountCredentials
import apiclient.discovery

# CREDENTIALS TO SERVICE ACC
CREDSTOSERVICE = 'credentials.json'
spreadsheet_id = '1BIJukq0TZt0RBi5JvjR3WGk3To1T-uZ3s3gNgfsydog'

class Reporting:

    def __init__(self):
        pass

    def auth(self):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            CREDSTOSERVICE,
            ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive'])
        httpauth = credentials.authorize(httplib2.Http())
        service = apiclient.discovery.build('sheets', 'v4', http=httpauth)

        return service

    @staticmethod
    def put_values(self):
        values = service.spreadsheets().values().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body={
                "valueInputOption": "USER_ENTERED",
                "data": [
                    {"range": "Sheet1!A1:P",
                     "majorDimension":"ROWS",
                     "values": result}
                ]
            }
        ).execute()


# Создаем коннектор к файлу нашей базы данных.
# Само собой, файлик Базы Данных должен лежать рядом с файлом блокнота (который вы сейчас читаете).
con = sqlite3.connect('DBname_hr.db')


cur = con.cursor()

# Создаем таблицу

cur.execute("""CREATE TABLE IF NOT EXISTS employees (
                contact_id INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT
                                        );""").fetchall()

cur.execute("""INSERT INTO employees (contact_id, first_name, last_name, email)
                        VALUES
                        (1, 'Bud', 'Powell', 'test@test.ru'), 
                        (2, 'Jan', 'Tax', 'test1@test.ru'),
                        (3, 'Max', 'Roberts', 'test2@test.ru'),
                        (4, 'Jannet', 'Wood', 'test3@test.ru')
                        ;""").fetchall()

result = pd.DataFrame(data=cur.execute('SELECT * FROM employees').fetchall())

r = Reporting()

# Вызовем авторизацию
service = r.auth()

# Объект перед отправкой по сети должен поддерживать сериализацию.
# К сожалению pd DataFrame ее не поддерживает, но мы можем извлечь значения

result = result.values.tolist()


# вызов метода put_values вставит объект result в нужную гугл-таблицу
r.put_values(r)

