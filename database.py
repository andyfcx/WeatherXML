from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
Base = declarative_base()

# i=1 1/1 1 station id, date, hour 
# I=1 1/1 2
# i=1 1/1 3
# ...
# i=1 1/1 24
# {'station': '466910', 'stname': '鞍部', 'datepicker': '2018-01-01', 'ObsTime': 24.0, 'StnPres': 927.3, 'SeaPres': 1552.8, 'Temperature': 11.6, 'Td dew point': 11.4, 'RH': 99.0, 'WS': 3.5, 'WD': 190.0, 'WSGust': 12.2, 'WDGust': 140.0, 'Precp': 'T', 'PrecpHour': 0.5, 'SunShine': '...', 'GloblRad': 0.0, 'Visb': '...', 'UVI': 0.0, 'Cloud Amount': '...'}
class WeatherData(Base):
    __tablename__ = "WeatherData"
    id = Column(Integer, primary_key=True)
    station = Column(String)
    stname = Column(String)
    date = Column(Date) # datepicker
    hour = Column(Integer) # ObsTime
    StnPres = Column(Float)
    SeaPres = Column(Float)
    Temperature = Column(Float)
    Dew = Column(Float)
    RH = Column(Float)
    WS = Column(Float)
    WD = Column(Float)
    WSGust = Column(Float)
    WDGust = Column(Float)
    Precp = Column(String)
    PrecpHour = Column(Float)
    SunShine = Column(String)
    GloblRad = Column(Float)
    Visb = Column(Float)
    UVI = Column(Float)
    Cloud = Column(String)



    
