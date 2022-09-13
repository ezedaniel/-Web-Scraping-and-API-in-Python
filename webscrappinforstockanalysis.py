import pandas as pd
import requests
from bs4 import BeautifulSoup
# Using the reqest to download the webpage to be analysed
html_data = " https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"

data = requests.get(html_data).text
#parse the text into html using beautiful_soup
soup = BeautifulSoup(data, 'lxml')
#we can turn the html table into a pandas dataframe
netflix_data = pd.DataFrame(
    columns=["Date", "Open", "High", "Low", "Close", "Volume"])

# First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text

    # Finally we append the data of each row to the table
    netflix_data = netflix_data.append({"Date": date, "Open": Open, "High": high, "Low": low,
                                       "Close": close, "Adj Close": adj_close, "Volume": volume}, ignore_index=True)

# we can print out the data frame here
netflix_data.head()
#We can also use the pandas read_html function using the url
read_html_pandas_data = pd.read_lxml(html_data)
#Or we can convert the BeautifulSoup object to a string
read_html_pandas_data = pd.read_html(str(soup))
netflix_dataframe = read_html_pandas_data[0]

netflix_dataframe.head
