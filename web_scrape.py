from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    query = data['queryResult']['queryText']

    # Set up the Selenium WebDriver (Chrome)
    driver = webdriver.Chrome()

    # Navigate to the WHO data collections URL
    search_url = "https://www.who.int/data/collections"
    driver.get(search_url)

    # Find the search bar element and input the user's query
    box = driver.find_element(By.XPATH, '//*[@id="PageContent_C035_Col00"]/label/input')
    box.send_keys(query)
    box.send_keys(Keys.RETURN)
    time.sleep(5)

    # Locate the first search result link and retrieve its URL
    first_result_link = driver.find_element(By.CSS_SELECTOR, "#collections > div:nth-child(14) > div > a")
    first_result_url = first_result_link.get_attribute("href")
    
    # Close the browser
    driver.close()

    # Create a response for Dialogflow
    response = {
        'fulfillmentText': f'First search result URL for {query}: {first_result_url}'
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
