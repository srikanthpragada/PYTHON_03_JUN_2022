import requests

try:
    resp = requests.get("http://worldclockapi.com/api/json/utc/now")
    if resp.status_code != 200:
        print("Sorry! Could not get details")
        exit()

    details = resp.json()  # JSON to dict
    print(details['currentDateTime'])
except:
    print("Sorry! Could not access server!")

