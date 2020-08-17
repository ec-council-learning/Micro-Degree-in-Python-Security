import sqlite3
from sqlite3 import Error


# DATABASE_MEMORY = ':memory:'
DATABASE_MEMORY = 'python-methods.db'


def run_query(create_table_sql):
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        return cursor
    except Error as e:
        print(e)


def insert_album(artist, title, genre, year):
    query = '''INSERT INTO "albums" ("Album", "Genre", "Artist" ,"year")
        VALUES ('{}', '{}', '{}', {})'''.format(
        artist, title, genre, year)
    run_query(query)


def select_albums(where=None):
    if where:
        query = '''SELECT * FROM "albums" WHERE {}'''.format(where)
    else:
        query = '''SELECT * FROM "albums"'''
    cursor = run_query(query)
    return cursor.fetchall()


def main():
    run_query('''
        CREATE TABLE IF NOT EXISTS "albums"
        (
            [id] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            [Artist] NVARCHAR(120),
            [Album] NVARCHAR(120) NOT NULL,
            [Genre] NVARCHAR(120) DEFAULT 'Rock',
            [year] INTEGER
        )
        ''')

    insert_album('AC/DC', 'For Those About To Rock We Salute You', 'Rock', 1981)
    insert_album('AC/DC', 'Let There Be Rock', 'Rock', 1977)
    insert_album('AC/DC', 'Back in Black', 'Rock', 1980)
    insert_album('Physical Graffiti [Disc 1]', 'Rock', 'Led Zeppelin', 1975)
    insert_album('Houses Of The Holy', 'Rock', 'Led Zeppelin', 1973)
    insert_album('In Through The Out Door', 'Rock', 'Led Zeppelin', 1979)

    rows = select_albums()
    print('Results from select all albums:')
    for row in rows:
        print(row)

    rows = select_albums('"year" BETWEEN 1970 AND 1978')
    print('Results from select albums between 1970 and 1978:')
    for row in rows:
        print(row)


if __name__ == '__main__':
    conn = sqlite3.connect(DATABASE_MEMORY)
    main()
    conn.close()
