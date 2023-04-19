import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from osim.io import io

angle, engine, body, nose_type = io.getSystemArg()
print(angle)
print(engine)
print(body)
print(nose_type)
