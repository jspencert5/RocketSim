
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



from osim.database.Database import Parts

print(sys.argv[1])

db = Parts()

print(db.getEngine("Estes E12"))
print(db.getBody("?"))
