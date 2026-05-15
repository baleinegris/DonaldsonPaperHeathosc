#### Preamble ####
# Purpose: Download the Toronto Apartment Building Registration dataset from Open Data Toronto
# Author: Oscar Heath
# Date: May 6th 2026
# Contact: oscar.heath@mail.utoronto.ca
# License: MIT
# Pre-requisites: 
  # - `pandas` must be installed (pip install pandas)
  # - `requests` must be installed (pip install requests)
  # - `io` must be installed (pip install io)



import requests
import pandas as pd 
from io import StringIO

# Boilerplate data import code from Open Data Toronto: https://open.toronto.ca/dataset/apartment-building-evaluation/

# Toronto Open Data is stored in a CKAN instance. It's APIs are documented here:
# https://docs.ckan.org/en/latest/api/

# To hit our API, you'll be making requests to:
	
base_url = "https://ckan0.cf.opendata.inter.prod-toronto.ca"
	
 	
# Datasets are called "packages". Each package can contain many "resources"
# To retrieve the metadata for this package and its resources, use the package name in this page's URL:
	
url = base_url + "/api/3/action/package_show"
	
params = { "id": "apartment-building-evaluation"}
	
package = requests.get(url, params = params).json()

# To get resource data:
for idx, resource in enumerate(package["result"]["resources"]):

       # for datastore_active resources:
       if resource["datastore_active"]:
            # To get all records in CSV format:
            url = base_url + "/datastore/dump/" + resource["id"]
            raw_df = pd.read_csv(StringIO(requests.get(url).text))

            ### I (Oscar Heath) added this code to save the raw data as a csv file ###
            if idx == 0:
                raw_df.to_csv("../data/01-raw_data/post2023_raw_data.csv", index=False)
                print(f"Saved {len(raw_df)} rows")
            else:
                raw_df.to_csv("../data/01-raw_data/pre2023_raw_data.csv", index=False)
                print(f"Saved {len(raw_df)} rows")