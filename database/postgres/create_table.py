import psycopg2


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = [
        '''CREATE TABLE conversation(
        id SERIAL PRIMARY KEY ,
        speaker VARCHAR(50),
        text VARCHAR(100) NOT NULL,
        datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );'''
    ]
    return commands


if __name__ == '__main__':
    create_tables()