from bs4 import BeautifulSoup as soup #parsing
from urllib.request import urlopen as uReq #requesting url

my_url = 'https://store.steampowered.com/app/1091500/Cyberpunk_2077/' #Paste any link u want

#looking for url and scanning suiteble html of the page with the set above url
uClient = uReq(my_url)

#Turning html into text-variable
page_html = uClient.read()

uClient.close()

#html parser
page_soup = soup(page_html , "html.parser") #parsing html into html(not xml,json and so on)

page_soup__directItem = page_soup.findAll("div",{"class":"game_purchase_price price"})#looking for every div with class on the page "game_description_snippet" 
directItem__content = page_soup__directItem[0].text.strip() #Getting exact value of the container

print("Actual product price:",directItem__content)