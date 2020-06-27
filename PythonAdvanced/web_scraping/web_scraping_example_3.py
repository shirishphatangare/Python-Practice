import requests
from bs4 import BeautifulSoup

page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')

# The find_all() method scans the entire document looking for results, but sometimes you only want to find one result. Use find() for such cases
seven_day = soup.find(id="seven-day-forecast")

# The find_all() method looks through a tag’s descendants and retrieves all descendants that match your filters
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
print(tonight.prettify())
print("--------------------------------")
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
print(period)
print(short_desc)
print(temp)
print("--------------------------------")
img = tonight.find("img")
desc = img['title']
print(desc)
print("----------------------------------")
# select() - If you want to search for tags that match two or more CSS classes, you should use a CSS select
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
print(periods)
print("-------------------------------------")

#get_text() - all text under the element
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
print(short_descs)
print(temps)
print(descs)