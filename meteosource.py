import requests
import pandas as pd
from tabulate import tabulate
import json

parameters = {
    "key":"si1b9x7ohpza3cs2ndwfj6tf5n18gdhjxgjk7c14",
    "place_id":"london"
}

url = "https://www.meteosource.com/api/v1/free/point"

data = requests.get(url, parameters)
#data.status_code
#print(data.text)
dataList = data.json() # -> JSON to list or dictionary
dataJson = json.loads(data.text) # -> converts to dictionary

# ----------------------------------- DIMENSION TABLE -----------------------------------#
keys_for_dim = ['lat', 'lon', 'elevation', 'timezone', 'units']
###### DICTIONARY COMPREHENSION to filter some keys -> SELECT columns
cityInfo = {key: value for key, value in dataJson.items() if key in keys_for_dim}
#create a dataframe for this table
df_cityInfo = pd.json_normalize(cityInfo)
#print(df_cityInfo)

# ----------------------------------- CURRENT TABLE -----------------------------------#
keys_for_current = ['current']
current = {key: value for key, value in dataJson.items() if key in keys_for_current}
df_current = pd.json_normalize(current)
print(current)
#print(dataList)
#print("Current temperature in London is {}".format(data['current']['temperature']))

#tentativo di normalizzare solo alcune colonne df = pd.json_normalize(dataList, 'lat', 'lon', 'elevation', 'timezone', 'units')

#print(df)

#get hourly data
#dfHour = df.explode()