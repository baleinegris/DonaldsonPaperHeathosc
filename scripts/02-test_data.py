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

# check that all of the comments have data types we would expect
assert(dtypes['year_built'] == 'int64') # check that year_built is an integer
assert(dtypes['storeys'] == 'int64') # check that num_stories is an integer
assert(dtypes['units'] == 'int64') # check that num_units is an integer
assert(dtypes['latitudes'] == 'float64') # check that latitudes is a float
assert(dtypes['longitudes'] == 'float64') # check that longitudes is a float

# check some sensible validation rules, for instance year is between 1900 and 2020, number of stories and units are positive
assert(sim_df["year_built"].max() <= 2020 and sim_df["year_built"].min() >= 1900) # check that year_built is between 1900 and 2020
assert(sim_df["storeys"].min() >= 1 and sim_df["units"].min() >= 1) # check that num_stories and num_units are positive