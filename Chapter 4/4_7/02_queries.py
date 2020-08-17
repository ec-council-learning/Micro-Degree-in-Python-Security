from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, sessionmaker, relationship


DATABASE_FILE = 'sqlalchemy_base.db'


Base = declarative_base()


class Artist(Base):
    __tablename__ = 'Artist'

    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


class Album(Base):
    __tablename__ = 'Album'

    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey('Artist.ArtistId'))

    artist = relationship(
        Artist,
        backref=backref('Album',
                        uselist=True,
                        cascade='delete,all'))


# Create database file
db = create_engine('sqlite:///{}'.format(DATABASE_FILE), echo=True)
Base.metadata.bind = db
Base.metadata.create_all()


# Bind to database to query
Session = sessionmaker(bind=db)
ses = Session()

# Populate data
artist = Artist(Name='AC/DC')
ses.add(artist)
ses.commit()

ses.add_all([
    Album(Title='For Those About To Rock We Salute You', ArtistId=artist.ArtistId),
    Album(Title='Let There Be Rock', ArtistId=artist.ArtistId),
    Album(Title='Back in Black', ArtistId=artist.ArtistId),
])
ses.commit()


artist = Artist(Name='Led Zeppelin')
ses.add(artist)
ses.commit()

ses.add_all([
    Album(Title='Physical Graffiti [Disc 1]', ArtistId=artist.ArtistId),
    Album(Title='Houses Of The Holy', ArtistId=artist.ArtistId),
    Album(Title='In Through The Out Door', ArtistId=artist.ArtistId),
])
ses.commit()

# Query Data
res = ses.query(Album).all()
for album in res:
    print(album.artist.Name, ' - ', album.Title)


# Complex Queries
res = ses.query(Album).join(Artist).all()
for album in res:
    print(album.artist.Name, ' - ', album.Title)

res = ses.query(Album).join(Album.artist).filter(Artist.Name.startswith('A')).all()
for album in res:
    print(album.artist.Name, ' - ', album.Title)
