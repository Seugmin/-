import requests
import lxml
from bs4 import BeautifulSoup

url = "https://kups.club/"


session = requests.Session()
header = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36"}

response = session.get(url, headers=header)
soup = BeautifulSoup(response.text, "lxml")

all_product = soup.find("div", class_="row mt-4")

products = all_product.find("div", class_="col-lg-4 col-md-4 col-sm-6 portfolio-item")
print(products.text)