import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/gdp/nepal-gdp/"
html = requests.get(url).content

tree = BeautifulSoup(html, 'html.parser')

tbody = tree.find('tbody')

table_rows = tbody.find_all('tr')

whole_data = []
for tr in table_rows:
    yearly_data = []
    td = tr.find_all('td')
    
    for item in td:
        yearly_data.append(item.text.strip())
        
    
    whole_data.append(yearly_data)



column_names = [item.text.strip() for item in tree.find('thead').find_all('th')]



import pandas as pd
df = pd.DataFrame(whole_data)
df = pd.DataFrame(whole_data, columns = column_names)
df.to_csv('gdp.csv', index = False)




