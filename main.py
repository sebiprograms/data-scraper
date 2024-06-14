import requests
from bs4 import BeautifulSoup
import pandas as pd

current_page = 1

page = requests.get(url)

print(page.text)

soup = BeautifulSoup(page.text,"html.parser")

proceed = True
# collect data while proceed is true
while(proceed):
  url = "https://books.toscrape.com/catalogue/page-"+str(current_page)+".html"
  if (soup.title.text == "404 Not Found"):
    proceed = False
  else:
    all_books = soup.find_all("li",class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
    
  current_page += 1