# import required modules
from bs4 import BeautifulSoup
import requests
 
# get URL
page = requests.get("https://en.wikipedia.org/wiki/List_of_districts_of_Jharkhand")
 
# scrape webpage
soup = BeautifulSoup(page.content, 'html.parser')
 
list(soup.children)
 
# find all occurrence of p in HTML
# includes HTML tags
print(soup.find_all('td'))
 
print('\n\n')
 
# return only text
# does not include HTML tags
print(soup.find_all('td')[0].get_text())
