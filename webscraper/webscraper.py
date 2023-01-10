import requests
import time
from bs4 import BeautifulSoup

URL = "https://www.amazon.com.au/RUMOURS-LP-FLEETWOOD-MAC/dp/B004OKFISQ/ref=sr_1_1?keywords=fleetwood+mac+rumours+vinyl&qid=1672968265&sprefix=fleetwood+mac+rumours%2Caps%2C343&sr=8-1"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

while True:
  try:
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    price_element = soup.select_one('#priceblock_ourprice')
    if price_element:
      price = price_element.get_text()
      print(price)
    else:
      print("Unable to find price on page")
  except Exception as e:
    print("An error occurred:", e)
  time.sleep(5)
