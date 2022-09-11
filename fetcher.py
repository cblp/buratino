from decimal import Decimal
import requests
import xml.etree.ElementTree as ET

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
response = requests.get(url)
response.raise_for_status()

root = ET.fromstring(response.text)
r = [
    (
        valute.find("CharCode").text,
        Decimal(valute.find("Value").text.replace(",", "."))
            / Decimal(valute.find("Nominal").text)
    )
    for valute in root.findall("Valute")
]
print(r)
