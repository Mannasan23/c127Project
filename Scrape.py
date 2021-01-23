from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers = ["V_mag", "proper_name", "bayer_designation", "distance", "spectral_class", "mass", "radius", "luminosity"]
    planet_data = []
    soup = BeautifulSoup(browser.page_source, "html.parser")
    for td_tag in soup.find_all("td", attrs={"class", "exoplanet"}):
        tl_tags = ul_tag.find_all("tl")
        temp_list = []
        for index, tl_tag in enumerate(li_tags):
            if index == 0:
                temp_list.append(tl_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp_list.append(li_tag.contents[0])
                except:
                    temp_list.append("")
        planet_data.append(temp_list)
    browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
with open("scrapper_2.csv", "w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)
scrape()