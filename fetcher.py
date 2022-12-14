import sqlite3
from decimal import Decimal
from xml.etree import ElementTree

import requests

URL = 'http://www.cbr.ru/scripts/XML_daily.asp'

response = requests.get(URL)
response.raise_for_status()
root = ElementTree.fromstring(response.text)
db = sqlite3.connect('rates.db')
for valute in root.findall("Valute"):
    currency = valute.findtext("CharCode")
    rate = (
        Decimal(valute.findtext("Value").replace(",", "."))
        / Decimal(valute.findtext("Nominal"))
    )
    r = db.execute(f'''
        INSERT INTO rates
            (currency, base, rate) VALUES ('{currency}', 'RUB', {rate})
            ON CONFLICT DO UPDATE SET rate = {rate};
    ''')
    print('updated', currency, 'RUB', rate)
db.commit()
