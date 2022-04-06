from private import api_key
import requests


def apiCall():

    base_url = "https://newsdata.io/api/1/news?apikey=" + \
        api_key+"&category=science,politics,world,environment,business&country=in"
    print(base_url)
    response = requests.get(base_url)
    json_data = response.json() if response and response.status_code == 200 else None
    return json_data
