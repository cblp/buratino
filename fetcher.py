import requests
import xml.etree.ElementTree as ET

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
response = requests.get(url)
response.raise_for_status()

root = ET.fromstring(response.text)
print(root)
