from bs4 import BeautifulSoup as soup #парсит
from urllib.request import urlopen as uReq #реквустит url
my_url = 'https://store.steampowered.com/app/1091500/Cyberpunk_2077/'
#Ищет указанный url и сканирует соответсвующий html страницы с указанным url
uClient = uReq(my_url)

#Переврдит html в значение переменной
page_html = uClient.read()

uClient.close()

#html parser
page_soup = soup(page_html , "html.parser") #парсит html в html(не в xml,json и пр.)
#print(page_soup.p)
page_soup__directItem = page_soup.findAll("div",{"class":"game_description_snippet"})#ищет все элементы div на странице,с классом "game_description_snippet" 

print(page_soup__directItem)
