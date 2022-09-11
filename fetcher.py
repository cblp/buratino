import sqlite3
from decimal import Decimal
import requests
import xml.etree.ElementTree as ET

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
response = requests.get(url)
response.raise_for_status()
root = ET.fromstring(response.text)
db = sqlite3.connect('rates.db')
for valute in root.findall("Valute"):
    currency = valute.find("CharCode").text
    rate = (
        Decimal(valute.find("Value").text.replace(",", "."))
        / Decimal(valute.find("Nominal").text)
    )
    r = db.execute(f'''
        INSERT INTO rates
            (currency, base, rate) VALUES ('{currency}', 'RUB', {rate})
            ON CONFLICT DO UPDATE SET rate = {rate};
    ''')
    print(currency, rate, r)
db.commit()
