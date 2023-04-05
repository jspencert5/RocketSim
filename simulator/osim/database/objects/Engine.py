import os
from osim.database.objects.Base import Base
from sqlalchemy import Column, Integer, String, Float

class Engine(Base):
    
    __tablename__ = 'parts-Engine'
   
    id = Column(Integer, primary_key = True)
    name = Column(String)
    part = Column(String)
    mass = Column(Float)
    fuelMass = Column(Float)
    outerDiameter = Column(Float)
    length = Column(Float)
    profileName = Column(String)
