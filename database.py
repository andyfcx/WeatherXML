from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date
Base = declarative_base()
engine = create_engine("mysql+pymysql://root:andypersonal@127.0.0.1/")

meta = MetaData()

# engine.execute("CREATE DATABASE Weather") #create db
engine.execute("USE Weather") # select new db

weatherdata = Table('WeatherData', meta,
    Column('id', Integer, primary_key=True),
    Column('station', String(16)),
    Column('stname', String(16)),
    Column('datepicker', Date), # datepicker
    Column('ObsTime', Float(asdecimal=True)), # ObsTime
    Column('StnPres', Float(asdecimal=True)),
    Column('SeaPres', Float(asdecimal=True)),
    Column('Temperature', Float(asdecimal=True)),
    Column('Td dew point', Float(asdecimal=True)),
    Column('RH', Float(asdecimal=True)),
    Column('WS', Float(asdecimal=True)),
    Column('WD', Float(asdecimal=True)),
    Column('WSGust', Float(asdecimal=True)),
    Column('WDGust', Float(asdecimal=True)),
    Column('Precp', Float(asdecimal=True)),
    Column('PrecpHour', Float(asdecimal=True)),
    Column('SunShine', String(16)),
    Column('GloblRad', Float(asdecimal=True)),
    Column('Visb', String(16)),
    Column('UVI', Float(asdecimal=True)),
    Column('Cloud Amount',String(16)),
)

meta.create_all(engine)
