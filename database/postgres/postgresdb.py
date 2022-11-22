import psycopg2
import config
from database.postgres import create_table


class Database:
    """PostgreSQL Database class."""

    def __init__(self):
        self.host = config.host
        self.username = config.user
        self.password = config.password
        self.port = config.port
        self.dbname = config.database
        self.conn = None
        self.cur = None

    def connect(self):
        """Connect to a Postgres database."""
        if self.conn is None:
            try:
                self.conn = psycopg2.connect(
                    host=self.host,
                    user=self.username,
                    password=self.password,
                    port=self.port,
                    dbname=self.dbname
                )
                self.cur = self.conn.cursor()
                try:
                    commands = create_table.create_tables()
                    for command in commands:
                        self.cur.execute(command)

                except Exception as e:
                    pass
                # close communication with the PostgreSQL database server
                self.conn.commit()
                self.cur.close()

            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            # finally:
            #     print('Connection opened successfully.')

    def insert_rows(self, query):
        self.cur = self.conn.cursor()
        self.cur.execute(query)
        self.conn.commit()
        self.cur.close()

