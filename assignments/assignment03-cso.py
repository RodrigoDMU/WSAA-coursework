# ----------------------------------------------------------------------------------------------------------------------------------------
# Assignment 03
# ----------------------------------------------------------------------------------------------------------------------------------------
# - Write a program that retrieves the dataset for the `exchequer account (historical series)` from the CSO, and stores it into a file
# called `cso.json`.
#
# - Upload this program to the same repository you used for the first assignment;
# - Save this assignment as `assignment03-cso.ipynb`;
# - This program should not be a long one;
# - I don't need you to reformat or analyse the data in any way;
# - It should be about 10ish lines long (I have not counted).
#
# - You will need to find the dataset in [CSO.ie](https://www.cso.ie/en/index.html), try economic and then finance, then finance 
# indicators. yes it is difficult to find, that is part of the task, actually the easiest way to find it is search for it.
# ----------------------------------------------------------------------------------------------------------------------------------------
# Author: Rodrigo De Martino Ucedo
# ----------------------------------------------------------------------------------------------------------------------------------------

import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"  # API URL for the dataset
response = requests.get(url)
data = response.json()

with open("cso.json", "w") as f:
    json.dump(data, f, indent=4)

# END