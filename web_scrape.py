import requests
from bs4 import BeautifulSoup
import json

url_array = ["https://www.who.int/"]
accumulated_data = []
session = requests.Session()

for i in url_array:
    url = i
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = {
        "title": soup.find('h1').text if soup.find('h1') else "Title not found",
        "description": soup.find('p').text if soup.find('p') else "Description not found",
        "project_details": soup.find('div', {'class': 'project-details'}).text if soup.find('div', {'class': 'project-details'}) else "Project details not found",
        "latest_news": [item.text for item in soup.find_all('div', {'class': 'news-item'})],
        "upcoming_events": [event.text for event in soup.find_all('div', {'class': 'event'})]
        }
    accumulated_data.append(data)

json_data = json.dumps(accumulated_data)
with open('scraped_data.json', 'w') as json_file:
    json_file.write(json_data)