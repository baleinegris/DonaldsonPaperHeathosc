#### Preamble ####
# Purpose: Simulates a dataset of Toronto Apartment Building Registration
# Author: Oscar Heath
# Date: May 6th 2026
# Contact: oscar.heath@mail.utoronto.ca
# License: MIT
# Pre-requisites: 
  # - `pandas` must be installed (pip install pandas)
  # - `numpy` must be installed (pip install numpy)

import pandas as pd
import numpy as np

#### Workspace setup ####
np.random.seed(42)


### Simulating data
num_rows = 5000 # how many rows we are generating

year_built = np.random.randint(1950, 2026, num_rows) # vector of years built between 1950 and 2026
num_stories = np.random.randint(1, 50, num_rows) # vector of number of stories between 1 and 50
num_units = np.random.randint(1, 500, num_rows) # vector of number of units between 1 and 500
latitudes = np.random.uniform(43.5, 43.8, num_rows) # vector of latitudes in Toronto
longitudes = np.random.uniform(-79.5, -79.0, num_rows) # vector of longitudes in Toronto

sim_df = pd.DataFrame({
    'year_built': year_built,
    'num_stories': num_stories,
    'num_units': num_units,
    'latitudes': latitudes,
    'longitudes': longitudes
})


#### Save data ####
sim_df.to_csv("../data/00-simulated_data/simulated_data.csv", index=False)