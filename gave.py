from math import log
"""
    If I only want to use the log function in the math module:
        >>> from math import log
        >>> log(100, 10)
        >>> 2.0

    If I want to refer to math module as something else:
        >>> import math as poop
        >>> poop.log(100, 10)
        >>> 2.0
"""
import csv
import sys


""" VARS """
data = []
amu = 32
save_flag = False


def find_density(input_col):
    global save_flag
    if save_flag:
        densities.append(float(input_col))
        save_flag = False
    if float(input_col) == amu:
        # Save the next col if we find a match with neighboring amu
        save_flag = True


""" DO STUFF """

# The program checks for a command line argument
# It should be the name of the TAB file
filename = str(sys.argv[1])

# Open TAB file and save as a dictionary
try:
    with open(filename, 'rb') as tabfile:
        reader = csv.reader(tabfile, delimiter=' ', skipinitialspace=True)
        for row in reader:

            clean_row = []
            densities = []
            alt_sza = []

            for num, col in enumerate(row):

                # Remove erroneus data
                if (float(col) == 9.9999e4) or (float(col) <= 0):
                    # Revert save flag for densities
                    save_flag = False
                    continue

                # Store cols 6 and 7 as your altitudes and sza's respectively
                if 6 <= num <= 7:
                    alt_sza.append(round(float(col)))

                # Search for densities by finding the amu
                # Save flag causes the next col to be saved
                else:
                    find_density(col)

            # If not 0 aka if empty, then proceed
            if not len(densities):
                densities.append(-1.0)
            else:
                avg_density = sum(densities)/len(densities)
                densities = [log(avg_density, 10)]

            # Save clean data as one list
            # [altitude, sza, log of average density]
            clean_row = alt_sza + densities
            data.append(clean_row)
except IOError:
    print("Error opening file. Check your filename and try again.")
    exit()

x = []
y = []

for row in data:
    x.append(row[0])
    y.append(row[1])

from pylab import *
scatter(y, x)
show()
