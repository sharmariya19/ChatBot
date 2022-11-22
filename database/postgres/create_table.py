import checkword

global name


def create_tables():
    """ create tables in the PostgreSQL database"""
    global name
    commands = [
        f'''CREATE TABLE {name}(
        id SERIAL PRIMARY KEY ,
        speaker VARCHAR(50),
        text VARCHAR(100) NOT NULL,
        datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );'''
    ]
    return commands


def user_name(username):
    global name
    name = username

