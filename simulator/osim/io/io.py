
"""

I/O
Desc: will hold all of the i/o methods needed to read and write csv files


"""
import sys
import csv
from osim.database import Database


def getSystemArg():
    """
    getInputFile
    Desc: this will get all the needed data for a simulation from a CSV file
    Params:
        Path: String - path to the input csv file
    Returns: ?
    """
    angle = sys.argv[1]
    engine = Database.getEngine(sys.argv[2])
    body = Database.getBody(sys.argv[3])
    nose_type = Database.getNose(sys.argv[4])

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


