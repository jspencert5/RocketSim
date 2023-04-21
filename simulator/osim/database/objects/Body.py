from simulator.osim.database.objects.Base import Base
from sqlalchemy import Column, Integer, String, Float

class Body(Base):
    
    __tablename__ = 'parts-Body'
   
    id = Column(Integer, primary_key = True)
    name = Column(String)
    part = Column(String)
    mass = Column(Float)
    innerDiameter = Column(Float)
    outerDiameter = Column(Float)
    length = Column(Float)