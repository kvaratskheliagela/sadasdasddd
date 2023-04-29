import csv
import requests
from datetime import datetime
from bs4 import BeautifulSoup
import time
url = "https://biblusi.ge/" 
response = requests.get(url)
# while True:
#   if requests:
#     time.sleep(datetime.timdelta(seconds=20).total_seconds())
#   else:
#      time.sleep(1)
soup = BeautifulSoup(response.text, 'html.parser')
body = soup.find("body")
wrapper = body.find("div", id='__layout')
fb_reset = wrapper.find('div', {'class': 'fbreset'})
print(fb_reset)
with open('biblusi_data.csv', mode='w', newline='') as biblusi_file:
    fieldnames = ['time_stamp', 'data']
    writer = csv.DictWriter(biblusi_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'time_stamp': datetime.now(), 'data': fb_reset})


