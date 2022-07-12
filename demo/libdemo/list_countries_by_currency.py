import requests

currency = "EUR"

resp = requests.get("https://restcountries.com/v3.1/all")
countries = resp.json()  # list of dict

for c in countries:
    if 'currencies' in c and currency in c['currencies']:
        name = c['name']['common']
        print(f"{name:50}")
