from bs4 import BeautifulSoup, SoupStrainer
import requests
import re

# url="https://www.google.co.uk/search?q=vivaro+2008&dcr=0&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj-1cTw8LLZAhVEIMAKHao8DAcQ_AUICigB&biw=1440&bih=803&dpr=2"
#
# r=requests.get(url)
#
# r_txt = ''
#
# print(r_txt)

with open('vivaro_search.txt', 'r') as file:
    r_txt = file.read()


found = re.findall(r'{.+\"ou\".+}', r_txt)

for find in found:
    print(find)
