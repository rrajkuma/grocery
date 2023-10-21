import requests
from bs4 import BeautifulSoup

#my groceries! these are Chandler specific, as I can't seem to figure out how to make this adaptable to other cities yet
TJs = "https://www.traderjoes.com/home/products/category/food-8"

#grabs the data
resp = requests.get(TJs)
#and if I'm successful, makes Soup
if resp.ok:
    soup = BeautifulSoup(resp.content, 'html.parser')
    print(soup)