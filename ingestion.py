import pyodbc
import pandas as pd 
import requests as req 
from requests.models import PreparedRequest

#### USING PREPARED REQUESTS SO THAT THROUGH JSON YOU CAN SET THE URL ACCORDINGLY
re = PreparedRequest()

url = "http://api.weatherapi.com/v1/current.json"
params = {
    "key":"2a8c6acff70f4f4bb3a184006241506",
    "q":"Paris"
}

re.prepare_url(url, params)
re.url  #check url

r = req.get(re.url)
r.status_code

print(r.text)