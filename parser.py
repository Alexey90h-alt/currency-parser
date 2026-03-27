import requests
from bs4 import BeautifulSoup

def get_currencies():
    url = "https://www.cbr.ru/currency_base/daily/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    items = soup.find_all("tr")
    
    # Список валют, которые нам интересны
    targets = ["USD", "EUR"]
    
    print("--- Актуальный курс валют ---")
    
    for item in items:
        # Проверяем, есть ли в строке USD или EUR
        for target in targets:
            if target in item.text:
                data = item.find_all("td")
                name = data[3].text
                value = data[4].text
                print(f"✅ {name}: {value} руб.")

get_currencies()