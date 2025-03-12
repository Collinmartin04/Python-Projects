from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue' #put whatever website url here
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser') 

table = soup.find_all('table')[0]

world_titles = table.find_all('th')

world_tables_titles = [title.text.strip() for title in world_titles]

df = pd.DataFrame(columns = world_tables_titles)

column_data = table.find_all('tr')

for row in column_data:
    row_data = row.find_all('tr')
    individual_row_data = [data.text.strip() for data in row_data]


print(individual_row_data)
