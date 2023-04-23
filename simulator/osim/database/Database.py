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
            Body(name="Wood", part="Body", mass=50.2, innerDiameter= 24.1, outerDiameter=25.1, length=1219.2),
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

        #current_working_directory = os.path.abspath('.')

        #dir = current_working_directory + "\\Assets\\simulator\\osim\\database\\profiles\\"

        D12 = [(0.049,2.569),
                (0.116,9.369),
                (0.184,17.275),
                (0.237,24.258),
                (0.282,29.73),
                (0.297,27.01),
                (0.311,22.589),
                (0.322,17.99),
                (0.348,14.126),
                (0.386,12.099),
                (0.442,10.808),
                (0.546,9.876),
                (0.718,9.306),
                (0.879,9.105),
                (1.066,8.901),
                (1.257,8.698),
                (1.436,8.31),
                (1.59,8.294),
                (1.612,4.613),
                (1.65,0)]
        E12 = [(0.052,5.045),
                (0.096,9.910),
                (0.196,24.144),
                (0.251,31.351),
                (0.287,32.973),
                (0.300,29.910),
                (0.344,17.117),
                (0.370,14.414),
                (0.400,12.973),
                (0.500,11.712),
                (0.600,11.171),
                (0.700,10.631),
                (0.800,10.09),
                (0.900,9.73),
                (1.000,9.55),
                (1.101,9.91),
                (1.200,9.55),
                (1.300,9.73),
                (1.400,9.73),
                (1.500,9.73),
                (1.600,9.73),
                (1.700,9.55),
                (1.800,9.73),
                (1.900,9.73),
                (2.000,9.55),
                (2.100,9.55),
                (2.200,9.73),
                (2.300,9.19),
                (2.375,9.37),
                (2.400,5.95),
                (2.440,0.0)]
        E9 = [(0.046,1.913),
                (0.235,16.696),
                (0.273,18.435),
                (0.326,14.957),
                (0.38,12.174),
                (0.44,10.435),
                (0.835,9.043),
                (1.093,8.87),
                (1.496,8.696),
                (1.997,8.696),
                (2.498,8.696),
                (3.014,9.217),
                (3.037,5.043),
                (3.067,1.217),
                (3.09,0.0)]
        

        if (name == "Estes_D12.eng"):
            points = D12
        elif (name == "Estes_E12.eng"):
            points = E12
        else:
            points = E9

        """
        try:

            with open(dir + name, 'r') as f:
                print("Openning File...")
                for line in f.readlines():
                    points.append(line.strip().split(' '))
                    print(line)
        except Exception as e: 
            print(e)
            print("Could not open thrust profile...")
        """
        
        time = [float(p[0]) for p in points]
        thrust = [float(p[1]) for p in points]
        
        return (np.asarray(time), np.asarray(thrust))


    

