'''
Write a program to fetch data using http get and point out the number of holidays in england
and group them based on the year
'''

import json
from urllib.request import urlopen
url = "http://www.gov.uk/bank-holidays.json"
data_load = urlopen(url)
url_info = json.loads(data_load.read())
print(url_info)