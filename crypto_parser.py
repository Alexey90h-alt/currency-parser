import requests

def get_crypto_rates():
    # 1. Ссылка на API CoinGecko (наш надежный источник)
    url = "https://api.coingecko.com/api/v3/simple/price"
    
    # 2. Настраиваем параметры: какие монеты и в каких валютах нам нужны
    params = {
        'ids': 'bitcoin,ethereum,litecoin,solana',
        'vs_currencies': 'usd,rub'
    }
    
    try:
        # Отправляем запрос
        response = requests.get(url, params=params)
        data = response.json()
        
        print("\n" + "="*40)
        print("   🚀 АКТУАЛЬНЫЕ КУРСЫ КРИПТОВАЛЮТ   ")
        print("="*40)
        
        coins = [
            ('bitcoin', '₿ Bitcoin '),
            ('ethereum', 'Ξ Ethereum'),
            ('solana', '◎ Solana  '),
            ('litecoin', 'Ł Litecoin')
        ]
        
        # 4. Проходим циклом и выводим всё в едином стиле
        for coin_id, label in coins:
            usd_price = data[coin_id]['usd']
            rub_price = data[coin_id]['rub']
            
            # :.2f - округляет до 2 знаков
            # :, - добавляет запятую как разделитель тысяч (например, 65,000.00)
            print(f"{label}: ${usd_price:,.2f}  |  {rub_price:,.2f} руб.")
            
        print("="*40)
        print("✨ Данные обновлены успешно! ✨\n")
            
    except Exception as e:
        print(f"❌ Ой, возникла ошибка: {e}")


if __name__ == "__main__":
    get_crypto_rates()