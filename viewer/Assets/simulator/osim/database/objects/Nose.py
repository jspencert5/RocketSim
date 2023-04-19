from simulator.osim.database.objects.Base import Base
from sqlalchemy import Column, Integer, String, Float

class Nose(Base):
    
    __tablename__ = 'parts-Nose'
   
    id = Column(Integer, primary_key = True)
    name = Column(String)
    part = Column(String)
    mass = Column(Float)
    outerDiameter = Column(Float)
    length = Column(Float)
