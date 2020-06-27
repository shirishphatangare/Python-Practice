"""
4. Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.(https://www.nytimes.com/)
"""

import requests
from bs4 import BeautifulSoup
import pprint

def scrape_data(url):
    list_article_titles = []
    # Hit the request
    response = requests.get(url, timeout=10)
    # Create a beatuful soup tree structure from the content of the response from the server
    soup = BeautifulSoup(response.content, 'html.parser')
    #soup = BeautifulSoup(response.content, 'lxml')

    for div in soup.findAll('div', attrs={'class': 'css-debyuq e1voiwgp1'}):
        header = div.find('h2')
        if header:
            title = header.get_text()
            list_article_titles.append(title)
    return list_article_titles


if __name__=="__main__":
    url = "https://www.nytimes.com/"
    print("------------------")
    list_article_titles = scrape_data(url)
    print(f"Printing {len(list_article_titles)} Article Titles")

    for title in list_article_titles:
        print(title)