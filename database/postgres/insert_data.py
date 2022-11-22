import psycopg2
import datetime
from database.postgres import postgresdb


def insert_detail(name, speaker, text):
    sql = f"""INSERT INTO {name}(speaker, text)
                 VALUES('{speaker}', '{text}');"""
    db_obj = postgresdb.Database()
    db_obj.connect()
    db_obj.insert_rows(sql)

