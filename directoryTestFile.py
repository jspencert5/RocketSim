from simulator.osim.calculations.helpers.kinetics import calcThrust

'''
    Because of the getProfile function using the working directory, to properly test the retrieval of the thrust
    profile, a test file needed to be added. When called from the "osim" file, it will work properly as it is in
    the same working directory as this file
'''

calcThrust(.2)
