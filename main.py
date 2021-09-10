from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Integer

engine = create_engine("sqlite:///test_db.db")
#from pdb import set_trace; set_trace()
session = sessionmaker(bind=engine)()

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    username = Column(String, primary_key=True)
    password = Column(String)

    def __init__(self, username, password):
        self.username = username
        self.password = password

#class Mesure_log(Base):
  #  __tablename__ = "mesure_log"
 #   id = Column(Integer, primary_key=True)
  #  pub_date = Column(DateTime) TEXT
  #  sensor_type = Column(String) TEXT
  #  sensor_value = Column(Integer) REAL
  #  online_status = Column(Boolean) 

user = User("Damian", "some_password")
session.add(user)
session.commit()