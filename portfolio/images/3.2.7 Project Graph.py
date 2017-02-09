'''
Sextual violence in the Untided states
in the following code we are able to show 
how sexual violence in the united states 
has actually been on a decrease starting 
at 1993 to 2015.
'''

import numpy as np
import matplotlib.pyplot as plt


# Get the income/age data from CSV
datafile = open('cv15at01.csv','r')
data = datafile.readlines()

years=[]
rates=[]

for line in data[5:]: # Omit header lines
    year, rate = line.split(',')
    rates.append(rate[0:-1])
    years.append(year)


fig, ax  = plt.subplots(1, 1)
ax.plot(years, rates, 'ro')
ax.set_title('Years vs. Sexual Violence Crime Rates in\nUSA')
ax.set_xlabel('Years')
ax.set_ylabel('Rates (Percent)')



fig.show()