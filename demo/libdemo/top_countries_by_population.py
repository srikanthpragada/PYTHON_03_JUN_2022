import requests

resp = requests.get("https://restcountries.com/v3.1/all")
countries = resp.json()  # list of dict

for c in sorted(countries, key=lambda c: c['population'], reverse=True)[:10]:
    name = c['name']['common']
    population = c['population']
    print(f"{name:50}  {population:10}")
