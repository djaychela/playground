import urllib3
from bs4 import BeautifulSoup

year = input('Enter a year (YYYY) to search for the most popular film for that year')
url = f"http://www.imdb.com/search/title?release_date={year},{year}&title_type=feature"

ourUrl = urllib3.PoolManager().request('GET', url).data
soup = BeautifulSoup(ourUrl, "lxml")
print(soup.find('title').text)

movieList = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})

for idx, div_item in enumerate(movieList, 1):
    div = div_item.find('div', attrs={'class': 'lister-item-content'})

    header = div.findChildren('h3', attrs={'class': 'lister-item-header'})

    div2 = div_item.find('div', attrs={'class': 'inline-block ratings-imdb-rating'})

    rating_text = div2.find('strong').text
    movie_text = str((header[0].findChildren('a'))[0].contents[0].encode('utf-8').decode('ascii', 'ignore'))
    print(f'{idx}: {movie_text} - {rating_text}')

