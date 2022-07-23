import requests
import pandas as pd
from bs4 import BeautifulSoup


searchterm = 'Sony'
productlist = []
url = f'https://www.ebay.com/sch/i.html?_from=R40&_nkw=camera&_sacat=0&rt=nc&Brand={searchterm}&_dcat=31388&_pgn='
for page in range(1, 3):
    req = requests.get(url + str(page))
    soup = BeautifulSoup(req.text, 'html.parser')

    results = soup.find_all('div', {'class': 's-item__wrapper clearfix'})
    for items in results:
        title = items.find('h3', {'class': 's-item__title'}).text
        price = items.find('span', {'class': 's-item__price'}).text
        try : sold =  items.find('span', {'class': 's-item__dynamic s-item__additionalItemHotness'}).text
        except : sold = 'none'
        img = items.find('img', {'class': 's-item__image-img'})['src']
        link = items.find('a', {'class': 's-item__link'})['href']
        try : bids = items.find('span', {'class': 's-item__bids s-item__bidCount'}).text
        except : bids = 'none'

        product = {
            'Tittle': title,
            'Price': price,
            'Sold': sold,
            'Bids': bids,
            'Img': img,
            'Link': link
        }
        productlist.append(product)

# Writting File excel/csv
df = pd.DataFrame(productlist)
df.to_excel('output.xlsx', index=False)
print('Saved to Excel')
