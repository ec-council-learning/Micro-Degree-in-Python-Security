from sqlalchemy import create_engine, MetaData, select, Table


DATABASE_FILE = 'chinook.db'
db = create_engine('sqlite:///{}'.format(DATABASE_FILE))

with db.connect() as conn:
    meta = MetaData(db)
    tracks = Table('tracks', meta, autoload=True)

    stmt = select([tracks])
    results = conn.execute(stmt)

    print(results.fetchall())
