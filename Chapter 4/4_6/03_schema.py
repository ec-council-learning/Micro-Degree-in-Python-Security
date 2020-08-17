from sqlalchemy import (create_engine, Column, Integer, MetaData,
                        select, String, Table)


meta = MetaData()
artists = Table('artists', meta,
                Column('ArtistId', Integer, primary_key=True),
                Column('Name', String)
                )

DATABASE_FILE = 'sqlalchemy.db'
db = create_engine('sqlite:///{}'.format(DATABASE_FILE))

# Create tables
artists.create(db)


conn = db.connect()

conn.execute(artists.insert(), [
   {'Name': 'AC/DC'},
   {'Name': 'Led Zeppelin'}
])

stmt = select([artists])
conn.execute(stmt).fetchall()


# Drop tables
artists.drop(db)
