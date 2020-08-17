from sqlalchemy import create_engine, inspect, MetaData


DATABASE_FILE = 'chinook.db'
db = create_engine('sqlite:///{}'.format(DATABASE_FILE))

meta = MetaData()
meta.reflect(bind=db)

for table in meta.tables:
    print(table)


insp = inspect(db)
print(insp.get_table_names())
print(insp.get_columns("tracks"))
print(insp.get_primary_keys("tracks"))
print(insp.get_schema_names())
