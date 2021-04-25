import argparse
import requests
from bs4 import BeautifulSoup as bs

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
LANGUAGE = "en-US,en;q=0.5"


def get_weather_data(url):
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html = session.get(url)
    soup = bs(html.text, "html.parser")

    print(soup)

    result = {}
    # result['temp_now'] = soup.find("div", attrs={"id": "wob_loc"}).text
    # result['dayhour'] = soup.find("div", attrs={"id": "wob_loc"}).text
    # result['weather_now'] = soup.find("span", attrs={"id": "wob_dc"}).text
    return result


region = 'london'
URL = "https://www.google.com/search?lr=lang_en&ie=UTF-8&q=weather+" + region

data = get_weather_data(URL)
print("Weather for:", region)
print("Now:", data["dayhour"])
print(f"Temperature now: {data['temp_now']}°C")
print("Description:", data['weather_now'])
