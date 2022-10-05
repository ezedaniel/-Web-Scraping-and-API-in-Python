 #relevant libraries
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

def search_vancouver_craigslist(search_value):
   
    # getting the current day datetime
    today = datetime.today()

    # openning the site in selenium webdriver
    driver = webdriver.Firefox()
    driver.get(f'https://vancouver.craigslist.org/search/sss?sort=date&query={search_value}')

    # getting the items published in the site
    items = driver.find_elements(By.CSS_SELECTOR, '*[class^="result-image gallery"')
    # getting the dates related to each item
    dates = driver.find_elements(By.CSS_SELECTOR, 'time')

    # Search the items published on the current day and write it to the outfile.txt 
    with open('outfile.txt', 'w') as outfl:
        for d, item in zip(dates,items):
            # getting the item published date 
            published_date_attr = d.get_attribute('title')
            pb_date = datetime.strptime(published_date_attr, '%a %d %b %H:%M:%S %p')

            if (
                pb_date.day == today.day and 
                pb_date.month == today.month
                ):
                # getting the item link
                link = item.get_attribute('href')
                outfl.write(f'{link} \n'
                )
    driver.close()

if __name__ == '__main__':
    search_value = 'Norco bike'
    search_vancouver_craigslist(search_value)
