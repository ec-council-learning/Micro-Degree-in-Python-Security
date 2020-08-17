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


db = create_engine('sqlite:///{}'.format(DATABASE_FILE), echo=True)
Base.metadata.bind = db
Base.metadata.create_all()
