#What is Web Scraping?
#-Term used to describe the use of a program or algorithm to extract and process
# large amounts of data from the web.
#- To perform web scraping, you should also import the libraries:
# - urllib :module is used to open URLs
# - Beautiful Soup library's(bs4-version4): extract data from html files(used to
# parse the html, that is, take the raw html text and break it into Python objects.)

import csv
import requests
from bs4 import BeautifulSoup


def scrape_data(url):
    response = requests.get(url, timeout=10)
    #create a beatuful soup tree structure from the content of the response from the server
    soup = BeautifulSoup(response.content, 'html.parser')
    #search throught the beatufiful object soup to find the second table in the document
    # which contains the data we want
    table = soup.find_all('table')[1]
    rows = table.select('tbody > tr')
    header = [th.text.rstrip() for th in rows[0].find_all('th')]
    with open('resources/output.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        for row in rows[1:]:
            data = [th.text.rstrip() for th in row.find_all('td')]
            writer.writerow(data)


if __name__=="__main__":
    url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
    scrape_data(url)