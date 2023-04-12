
"""

I/O
Desc: will hold all of the i/o methods needed to read and write csv files


"""
import sys
import csv
import os
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from osim.database.Database import Parts


def getSystemArg():
    """
    getInputFile
    Desc: this will get all the needed data for a simulation from a CSV file
    Params:
        Path: String - path to the input csv file
    Returns: ?
    """
    db = Parts()
    angle = sys.argv[1]
    engine = db.getEngine(sys.argv[2])
    body = db.getBody(sys.argv[3])
    nose_type = db.getNose(sys.argv[4])

    return angle, engine, body, nose_type


def exportSimData(lines, path):
    """
    exportSimData
    Desc: exports simulation data to a csv for the viewer program to read
    Params: 
        lines: 2D Array - each array in the array is a line in the csv
    Returns: ?
    """
    with open(path, "w+") as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        csvWriter.writerows(lines)
    return 0


