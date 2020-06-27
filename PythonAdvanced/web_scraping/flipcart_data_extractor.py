import requests
from bs4 import BeautifulSoup

page=requests.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
content = page.content
soup = BeautifulSoup(content)

for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating=a.find('div', attrs={'class':'hGSR34'})
    products.append(name)
    prices.append(price)
    ratings.append(rating)
print("--------Products---------")
print(products)
print("--------Prices---------")
print(prices)
print("--------Ratings---------")
print(ratings)