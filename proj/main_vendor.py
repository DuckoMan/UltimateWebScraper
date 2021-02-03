from bs4 import BeautifulSoup as soup #parsing
from urllib.request import urlopen as uReq #requesting url

def scrapElement(url, tag , className):
    #looking for url ans scanning suiteble html of the page with the set above url
    uClient = uReq(url)
    #Turning html into text-variable
    page_html = uClient.read()

    uClient.close()

    #html parser
    page_soup = soup(page_html , "html.parser") #parsing html into html(not xml,json and so on)

    #print(page_soup.p)
    page_soup__directItem = page_soup.findAll(tag ,{"class": className }) #looking for every div with class on the page 'game_description_snippet'
    directItem__content = page_soup__directItem[0].text.strip() #Getting exact value of the container

    return directItem__content