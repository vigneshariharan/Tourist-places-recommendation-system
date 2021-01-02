import sys
import csv
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def calcreviews(url1):
    try:
        #code comes here
        driver.get(url1)
        driver.find_element_by_xpath(".//span[contains(@jscontroller,'h6wiFf')]").click()
        time.sleep(10)
        driver.find_element_by_xpath("/html/body/span/g-lightbox/div[2]/div[3]/span/div/div/div/div[1]/div[3]/div[2]/g-dropdown-menu/g-popup/div[1]/g-dropdown-button/span").click()
        driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[6]/div/g-menu/g-menu-item[2]").click()
        time.sleep(10)
        date_list = driver.find_elements_by_xpath(".//span[contains(@class, 'dehysf lTi8oc')]")
        stars_list = driver.find_elements_by_xpath(".//span[contains(@class, 'Fam1ne EBe2gf')]")
        count = 0
        total = 0.0
        maximum = 10
        for i in range(1,len(stars_list)):
            timeline = date_list[i-1].text
            if(timeline.find("month")==-1 and timeline.find("year")==-1):
                num=float(stars_list[i].get_attribute("aria-label").split(" ")[1])
                total+=num
                count+=1
        avg = round((total/count),2)
        avg = avg * count/maximum
        return avg
    except Exception as e:
        return 0.0

# default path to file to store data
path_to_file = "/home/ubuntuvm/fyp/reviews.csv"

# default tripadvisor website of hotel or things to do (attraction/monument) 
place=input()
url = "https://www.tripadvisor.com/Search?q="+place+"&ssrc=A"

# if you pass the inputs in the command line
if (len(sys.argv) == 4):
    path_to_file = sys.argv[1]
    num_page = int(sys.argv[2])
    url = sys.argv[3]

# import the webdriver	

profile = webdriver.FirefoxProfile()
# do whatever you want with the profile
driver = webdriver.Firefox(profile)

driver.get(url)

# open the file to save the review
csvFile = open(path_to_file, 'w', encoding="utf-8")
csvWriter = csv.writer(csvFile)

# change the value inside the range to save more or less reviews
# expand the review 
time.sleep(2)

#getting the urls
url_list = driver.find_elements_by_xpath(".//div[contains(@class,'result-title')]")
ratings = []


#getting the categories    
category_list = driver.find_elements_by_xpath(".//span[contains(@class, 'thumbnail-overlay-tag')]")
#getting the places
place_list = driver.find_elements_by_xpath(".//div[contains(@class, 'result-title')]")

places=[]
category=[]
for j in range(len(category_list)):
    category.append(category_list[j].text)
for i in range(len(place_list)):
    places.append(place_list[i].text)
    
for k in range(max(len(places),len(category))):
    cat=category[k]
    if(cat.find('Tours')==-1):
        pl=places[k]
        website = "https://www.google.com/search?q="+pl+" - "+place
        rat= calcreviews(website)    
        csvWriter.writerow([pl,cat,rat])

driver.quit()
