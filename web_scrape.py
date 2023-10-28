import requests
from bs4 import BeautifulSoup
import json

url_array = ["https://www.who.int/", "https://www.unicefusa.org/?form=donate&gad=1&gclid=Cj0KCQjw4vKpBhCZARIsAOKHoWSCEa_HxUtDkIhKAx2goONQzOQuurgo-nAocETXIqmiKymuDwm7JQkaAiKDEALw_wcB", "https://www.redcross.org/?cid=generic&med=cpc&source=google&scode=RSG00000E017&&&gclid=Cj0KCQjw4vKpBhCZARIsAOKHoWQU-8tFJPzcZPJxBy0RjVVllv4rCVkFGN_6qh9e53eJg6yahXZDxjcaAkEaEALw_wcB&gclsrc=aw.ds"]
accumulated_data = []

for i in url_array:
    url = i
    response = response.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = {

    }
    accumulated_data.append(data)

json_data = json.dumps(accumulated_data)
with open('scraped_data.json', 'w') as json_file:
    json_file.write(json_data)