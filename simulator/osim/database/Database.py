import os
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
import numpy as np

from simulator.osim.database.objects.Base import Base
from simulator.osim.database.objects.Body import Body
from simulator.osim.database.objects.Engine import Engine
from simulator.osim.database.objects.Nose import Nose


"""

Database Class
Desc: Allows us to query and access parts without additional parsing

"""

class Parts:

    def __init__(self):
        """
        init
        Desc: initilizes database of parts
        """

        self.engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

        Base.metadata.create_all(self.engine)

        self.loadDefaultParts()
        
    def loadDefaultParts(self):

        s = Session(self.engine)

        bodies = [
            Body(name="Clear Plastic", part="Body", mass=4.6, innerDiameter= 24.1, outerDiameter=24.8, length=152),
            Body(name="Fiberglass", part="Body", mass=97.8, innerDiameter= 24.1, outerDiameter=25.1, length=1219.2),
            Body(name="Paper", part="Body", mass=10.9, innerDiameter= 24.1, outerDiameter=24.8, length=457.2)
        ]
        

        noses = [
            Nose(name="PNC-24A", part="Nose", mass=4.6, outerDiameter=24.8, length=76.2),
            Nose(name="PNC-24C", part="Nose", mass=9.7, outerDiameter=24.8, length=104.8),
            Nose(name="PNC-24D", part="Nose", mass=7.5, outerDiameter=24.8, length=69.9),
        ]

        engines = [
            Engine(name="Estes D12", part="Engine", mass=44, fuelMass= 21.1, outerDiameter=24, length=70, profileName="Estes_D12.eng", maxBurnTime=1.65),
            Engine(name="Estes E12", part="Engine", mass=59, fuelMass= 35.8, outerDiameter=24, length=95, profileName="Estes_E12.eng", maxBurnTime=2.44),
            Engine(name="Estes E9", part="Engine", mass=58, fuelMass= 35.9, outerDiameter=24, length=95, profileName="Estes_E9.eng", maxBurnTime=3.09),
        ]

        s.bulk_save_objects(bodies)
        s.bulk_save_objects(noses)
        s.bulk_save_objects(engines)

        s.commit()

    def getEngine(self, name):

        s = Session(self.engine)
        return s.execute(select(Engine).where(Engine.name == name)).first()[0]

    def getBody(self, name):
        
        s = Session(self.engine)
        return s.execute(select(Body).where(Body.name == name)).first()[0]


    def getNose(self, name):
        
        s = Session(self.engine)
        return s.execute(select(Nose).where(Nose.name == name)).first()[0]
    
    def getProfile(self, name):
        
        points = []

        current_working_directory = os.path.abspath('.')
        dir = current_working_directory + "\\simulator\\osim\\database\\profiles\\"

        with open(dir + name, 'r') as f:
            for line in f.readlines():
                points.append(line.strip().split(' '))
        
        time = [float(p[0]) for p in points]
        thrust = [float(p[1]) for p in points]
        
        return (np.asarray(time), np.asarray(thrust))


    

