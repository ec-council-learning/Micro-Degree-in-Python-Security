import sqlite3


DATABASE_FILE = 'python.db'
conn = sqlite3.connect(DATABASE_FILE)
cursor = conn.cursor()

#  Create Table
cursor.execute('''CREATE TABLE "albums"
(
    [id] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [Artist] NVARCHAR(120),
    [Album] NVARCHAR(120) NOT NULL,
    [Genre] NVARCHAR(120) DEFAULT 'Rock'
)''')


#  Create Data
cursor.execute('''INSERT INTO "albums" VALUES
    ( 1, 'AC/DC', 'For Those About To Rock We Salute You', 'Rock')''')
cursor.execute('''INSERT INTO "albums" VALUES
    ( 2, 'AC/DC', 'Let There Be Rock', 'Rock')''')
cursor.execute('''INSERT INTO "albums" VALUES
    ( 3, 'AC/DC', 'Back in Black', 'Rock')''')


#  Create Data without assigning ID
cursor.execute('''INSERT INTO "albums" ( "Album", "Genre", "Artist")
    VALUES ( 'Physical Graffiti [Disc 1]', 'Rock', 'Led Zeppelin')''')
cursor.execute('''INSERT INTO "albums" ( "Album", "Genre", "Artist")
    VALUES ( 'Houses Of The Holy', 'Rock', 'Led Zeppelin')''')
cursor.execute('''INSERT INTO "albums" ( "Album", "Genre", "Artist")
    VALUES ( 'In Through The Out Door', 'Rock', 'Led Zeppelin')''')


#  Read Data
cursor.execute('''SELECT * FROM "albums" WHERE "artist" = 'AC/DC' ''')
print('Results from select * artist AC/DC:')
for row in cursor.fetchall():
    print(row)


#  Update Data
cursor.execute('''UPDATE "albums" SET "Genre"='Classic Rock' WHERE "Genre" = 'Rock' ''')


#  Delete Data
cursor.execute('''DELETE FROM "albums" WHERE "id" = 2''')


#  Alter Table add Column
cursor.execute('''ALTER TABLE albums ADD year INTEGER''')


#  Update Data with Album Year
cursor.execute('''UPDATE "albums" SET "year"=1981
    WHERE "artist"='AC/DC' AND "album"='For Those About To Rock We Salute You' ''')
cursor.execute('''UPDATE "albums" SET "year"=1977 WHERE id=2''')
cursor.execute('''UPDATE "albums" SET "year"=1980
    WHERE "artist"='AC/DC' AND "album"='Back in Black' ''')
cursor.execute('''UPDATE "albums" SET "year"=1975
    WHERE "artist"='Led Zeppelin' AND "album"='Physical Graffiti [Disc 1]' ''')
cursor.execute('''UPDATE "albums" SET "year"=1973
    WHERE "artist"='Led Zeppelin' AND "album"='Houses Of The Holy' ''')
cursor.execute('''UPDATE "albums" SET "year"=1979
    WHERE "artist"='Led Zeppelin' AND "album"='In Through The Out Door' ''')


#  SELECT between
cursor.execute('''SELECT * FROM "albums" WHERE "year" IN (1977, 1980, 1981)''')
print('Results from select * year 1977, 1980, 1981:')
print(cursor.fetchone())

cursor.execute('''SELECT * FROM "albums" WHERE "year" BETWEEN 1970 AND 1978''')
print('Results from select * year between 1970 and 1978')
for row in cursor.fetchmany(2):
    print(row)


#  Create 2nd Table
cursor.execute('''CREATE TABLE IF NOT EXISTS songs (
  [id] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  [Title] NVARCHAR(120),
  [AlbumId] INTEGER,
  FOREIGN KEY (AlbumId) REFERENCES albums (id)
)''')


#  Create Data 2nd Table
cursor.execute('''INSERT INTO "songs" ("Title", "AlbumId") VALUES
  ('For Those About to Rock (We Salute You)', 1),
  ('Inject the Venom', 1)''')


#  Insert and Select
cursor.execute('''INSERT INTO "songs" ("Title", "AlbumId")
    SELECT 'The Song Remains the Same', "id"
    FROM "albums" WHERE "album"='Houses Of The Holy' ''')


#  Read data with relationship
cursor.execute('''SELECT "albums".*, "songs".*
    FROM "songs"
    JOIN "albums" ON "songs"."AlbumId" = "albums"."id" ''')
print('Results from select * albums and songs:')
for row in cursor.fetchall():
    print(row)


conn.close()
