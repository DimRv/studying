import json
import requests

year = "2022"
url = 'https://raw.githubusercontent.com/d10xa/holidays-calendar/master/json/consultant' + year + '.json'
r = requests.get(url)
cal = json.loads(r.text)
print(cal["holidays"].count("2022-12-31"))