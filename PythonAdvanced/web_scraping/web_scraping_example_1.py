#What is Web Scraping?
#-Term used to describe the use of a program or algorithm to extract and process
#-Web scraping is also sometimes referred to as web harvesting or web data extraction.
# Copying text from a website and pasting it to your local system is also web scraping.
# However, it is a manual task. Generally, web scraping deals with extracting data
# automatically with the help of web crawlers. Web crawlers are scripts that connect to
# the world wide web using the HTTP protocol and allows you to fetch data in an
# automated manner.

#Potential Challenges of Web Scraping
#1)One of the challenges you would come across while scraping information from websites
# is the various structures of websites.The templates of websites will differ and will be
# unique; hence, generalizing across websites could be a challenge.
#2)Another challenge could be longevity. Since the web developers keep updating their
# websites, you cannot certainly rely on one scraper for too long. Even though the
# modifications might be minor, but they still might create a hindrance for you while
# fetching the data.
#- A solution to this would be approach is to use Application Programming Interfaces (APIs)
# offered by various websites & platforms.The format of the data when using APIs is
# different from usual web scraping i.e., JSON or XML, while in standard web scraping,
# you mainly deal with data in HTML format.

# large amounts of data from the web.
#- To perform web scraping, you should also import the libraries:
# - urllib :module is used to open URLs
# - Beautiful Soup library's(bs4-version4): extract data from html files(used to
# parse the html, that is, take the raw html text and break it into Python objects.)
#CommandLine: pip install beautifulsoup4
"""
Other Libraries:
#Selenium:  Selenium is a web testing library. It is used to automate browser activities.
#BeautifulSoup: Beautiful Soup is a Python package for parsing HTML and XML documents.
It creates parse trees that is helpful to extract the data easily.
#Pandas: Pandas is a library used for data manipulation and analysis.
It is used to extract the data and store it in the desired format.
"""

"""
To extract data using web scraping with python, you need to follow these basic steps:

    Find the URL that you want to scrape
    Inspecting the Page
    Find the data you want to extract
    Write the code
    Run the code and extract the data
    Store the data in the required format

"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.hubertiming.com/results/2017GPTR10K"
html = urlopen(url)
#soup = BeautifulSoup(html, 'lxml')
soup = BeautifulSoup(html, 'html.parser')

print("Type of Object:",type(soup))
# Get the title
title = soup.title
print("Title of the Page:",title)
# Print out the text
text = soup.get_text()
print(text)
print("Soup:",soup)