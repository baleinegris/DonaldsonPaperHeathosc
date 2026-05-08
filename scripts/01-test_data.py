#### Preamble ####
# Purpose: Tests simulated data of Toronto Apartment Building Registration
# Author: Oscar Heath
# Date: May 6th 2026
# Contact: oscar.heath@mail.utoronto.ca
# License: MIT
# Pre-requisites: 
  # - `pandas` must be installed (pip install pandas)


import pandas as pd

# Load the simulated data
sim_df = pd.read_csv("../data/00-simulated_data/simulated_data.csv")
num_rows = 5000 # how many rows we generated in 00-simulate_data.py

### Running some tests on the data ###
assert(len(sim_df) == num_rows) # check that we have the right number of rows

dtypes = sim_df.dtypes
assert(dtypes['year_built'] == 'int64') # check that year_built is an integer
assert(dtypes['num_stories'] == 'int64') # check that num_stories is an integer
assert(dtypes['num_units'] == 'int64') # check that num_units is an integer
assert(dtypes['latitudes'] == 'float64') # check that latitudes is a float
assert(dtypes['longitudes'] == 'float64') # check that longitudes is a float