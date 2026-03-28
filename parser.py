import requests
from bs4 import BeautifulSoup

def get_currencies():
    url = "https://www.cbr.ru/currency_base/daily/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    items = soup.find_all("tr")
    targets = ["USD", "EUR"]
    
    print("--- Актуальный курс валют ---")
    
    for item in items:
        for target in targets:
            if target in item.text:
                data = item.find_all("td")
                name = data[3].text
                value_num = float(data[4].text.replace(',', '.'))
                
                print(f"✅ {name}: {value_num:.2f} руб.")

get_currencies()