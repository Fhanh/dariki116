import sqlite3
from settings import *

conn = sqlite3.connect('users.db', check_same_thread=False)


def init_db(force: bool = False):
    c = conn.cursor()
    if force:
        c.execute('DROP TABLE IF EXISTS users_data')

    c.execute('''
            CREATE TABLE IF NOT EXISTS users_data (
                id              INTEGER PRIMARY KEY,
                user_name       TEXT NOT NULL,
                user_id         INTEGER NOT NULL,
                goods_page      INTEGER NOT NULL
            )
        ''')
    conn.commit()
    c.close()


def db_check_user(user_id: int, user_name: str):
    c = conn.cursor()
    c.execute('SELECT user_id FROM users_data WHERE user_id = ?', (user_id, ))
    selected = c.fetchone()
    if not selected:
        db_add_user(user_name, user_id, 1)
        logger.info(f"Added to the database---> {time} | {user_id} | {user_name}")


def db_add_user(user_name: str, user_id: int, goods_page: int):
    c = conn.cursor()
    c.execute('INSERT INTO users_data (user_name, user_id, goods_page) VALUES (?, ?, ?)', (user_name, user_id,
                                                                                           goods_page))
    conn.commit()
    c.close()


def db_select_page(user_id: int):
    c = conn.cursor()
    c.execute('SELECT goods_page FROM users_data WHERE user_id = ?', (user_id, ))
    selected = c.fetchone()
    c.close()
    return selected[0]


def db_change_page(goods_page: int, user_id: int):
    c = conn.cursor()
    c.execute('UPDATE users_data SET goods_page = ?  WHERE user_id = ?', (goods_page, user_id))
    conn.commit()
    c.close()


def db_select_users_ids():
    c = conn.cursor()
    c.execute('SELECT user_id FROM users_data')
    selected = c.fetchall()
    c.close()
    return selected
