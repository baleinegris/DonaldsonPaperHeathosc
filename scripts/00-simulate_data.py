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
# set seed for reproducibility
np.random.seed(42)

### Simulating data ###
num_rows = 5000 # how many rows we are generating

baseline_buildings = 3000 # baseline number of units, we will add to this based on the year built
extra_buildings_post_war = 1250 # number of extra buildings we will add to post war period based on the year built
extra_buildings_contemporary = 750 # number of extra buildings we will add to contemporary period based on the year built
# Note: baseline_buildings + extra_buildings_post_war + extra_buildings_contemporary should equal num_rows

year_built = np.random.randint(1900, 2020, baseline_buildings) # baseline vector of buildings built between 1900 and 2020
extra_post_war = np.random.randint(1950, 1970, extra_buildings_post_war) # vector of extra buildings built between 1950 and 1970
extra_contemporary = np.random.randint(2000, 2020, extra_buildings_contemporary) # vector of extra_buildings built between 2000 and 2020

year_built = np.concatenate([year_built, extra_post_war, extra_contemporary]) # vector of buildings between 1900 and 2020

num_stories = np.random.randint(1, 30, num_rows) # baseline vector of number of stories between 1 and 30

# uniformly distributed lats and longs in Toronto, roughly corresponding to these values
latitudes = np.random.uniform(43.5, 43.8, num_rows) # vector of latitudes in Toronto
longitudes = np.random.uniform(-79.5, -79.0, num_rows) # vector of longitudes in Toronto

sim_df = pd.DataFrame({
    'year_built': year_built,
    'storeys': num_stories,
    'latitudes': latitudes,
    'longitudes': longitudes
})

# apartments today are taller and have more units, so add some correlation between year built and number of stories and units
sim_df['storeys'] = sim_df['storeys'] + (sim_df['year_built'] - 1900) // 10 * 2 # add 2 storeys for every 10 years after 1900

num_units = sim_df["storeys"] * 10 + np.random.randint(1, 50, num_rows) # number of units assumed to be rougly 10 times number of stories, with some noise
sim_df['units'] = num_units


#### Save data ####
sim_df.to_csv("../data/00-simulated_data/simulated_data.csv", index=False)