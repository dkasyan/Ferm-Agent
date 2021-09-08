import sqlalchemy
from sqlalchemy.sql.sqltypes import DateTime
from config import Config

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import inspect



def create_db_eng():
    create_engine('sqlite:///BASE_DIR/testDB.db')
    print("Stworzylem tabele")
    metadata = MetaData()
    books = Table('mesure', metadata,
        Column('id', Integer, primary_key=True),
        Column('pub_date', DateTime),
        Column('sensor_type', String),
        Column('sensor_value', String),
        Column('online_status')
        )

    engine = create_engine('sqlite:///testDB.db')
    metadata.create_all(engine)

create_db_eng()