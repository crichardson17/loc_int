#
# Read / Return emission line output and parameter sweep variables
#

import csv
from numpy import *

var1,var2 = 6,7

def parser(gridfile,emisfile,normline):

    griddata, emisdata = [], []

    with open(gridfile, 'rb') as f:
        csvReader = csv.reader(f, delimiter='\t')
        gridheaders = csvReader.next()
        for row in csvReader:
            griddata.append(row);
        griddata = asarray(griddata)
    

    phi = 10**array(griddata[:,var1],float) # Need to convert to linear
    hden = 10**array(griddata[:,var2],float)
            
    with open(emisfile, 'rb') as f:
        csvReader = csv.reader(f, delimiter='\t')
        emisnames = csvReader.next()
        for row in csvReader:
            emisdata.append(row);
        emisdata = asarray(emisdata)

    emisdata = array(emisdata, float)

    grid_size = len(emisdata[:,0])
    num_of_lines = len(emisdata[0,:])

    normloc = emisnames.index(normline)
    normdata = emisdata[:, normloc]

    return phi, hden, emisnames, emisdata, normdata, grid_size, num_of_lines
