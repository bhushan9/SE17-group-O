import requests
import json

r=requests.get('https://newsapi.org/v1/articles?source=techcrunch&apiKey=a97466277811418284e9525947633cbd')

z= ''
z= r.json()



print(len(z["articles"]))

with open('data.txt', 'w') as outfile:
    json.dump(r.json(), outfile)

