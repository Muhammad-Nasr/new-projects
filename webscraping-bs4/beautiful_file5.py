from bs4 import BeautifulSoup
import requests
import re

url = 'https://keithgalli.github.io/web-scraping/webpage.html'

page = requests.get(url)

soup =BeautifulSoup(page.text, 'html.parser')

# look for all h1, h2, h3

headers = soup.find_all(['h1', 'h2', 'h3'])

#print(headers)

div = soup.find(class_='fun-facts')

# use regular expression 
text = div.find(text=re.compile('dream'))
text = div.find_all(text=re.compile('d|D'))


# use select 
paragraphs = soup.select("body > p")
print(paragraphs)

for paragraph in paragraphs:
  print(paragraph.select("i"))

soup.select("[align=middle]")

 #------------ 
files = page.select("div.block a")
relative_files = [f['href'] for f in files]


url = "https://keithgalli.github.io/web-scraping/"
for f in relative_files:
  full_url = url + f
  page = requests.get(full_url)
  bs_page = bs(page.content)
  secret_word_element = bs_page.find("p", attrs={"id": "secret-word"})
  secret_word = secret_word_element.string
  print(secret_word)








