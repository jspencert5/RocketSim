
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



from osim.database.Database import Parts

db = Parts()

eng = db.getEngine("Estes E12")
print(eng.profileName)
print(db.getProfile(eng.profileName))
