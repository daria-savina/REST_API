import requests
from  api import API_KEY
import json
from pprint import pprint


endpoint = "https://api.giphy.com/v1/gifs/trending"
params = {"api_key": API_KEY, "limit": 5, "rating": "g"}

response = requests.get(endpoint, params=params).json()
filename = 'data.json'

for gif in response['data']:
    id = gif['id']
    title = gif['title']
    trending_date = gif['trending_datetime']
    url = gif['url']
    entry = {'id': gif['id'], 'title': gif['title'], 'date': gif['trending_datetime'], 'url': gif['url']}
    jsonString = json.dumps(entry)
    jsonFile = open(filename, "w", encoding='utf-8')
    jsonFile.write(jsonString)
    jsonFile.close()

    with open('data.json', 'r', encoding='utf-8') as f:
        text = json.load(f)
        pprint(text)












