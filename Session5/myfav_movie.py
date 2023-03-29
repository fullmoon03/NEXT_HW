from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import csv


# 디버깅 모드
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = './chromedriver'
driver = webdriver.Chrome(chrome_driver, options= chrome_options)

#csv 생성
file = open('myfav_movie.csv', mode="w", newline='')
writer = csv.writer(file)
writer.writerow(["title", "director", "ratings_num", "reviewers_num"])

# 실행할 웹페이지 불러오기 (네이버 영화)
driver.get("https://movie.naver.com/")
searchbox = driver.find_element(By.XPATH, '//*[@id="ipt_tx_srch"]')
time.sleep(1)
searchbox.send_keys("노트북")
time.sleep(1)
searchbox.send_keys(Keys.ENTER)
time.sleep(1)

moviebtn = driver.find_element(By.XPATH, '//*[@id="old_content"]/ul[2]/li[3]/dl/dt/a')
moviebtn.click()

title = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/h3/a').text
director = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
ratings_num = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[2]/div[1]/div/span/em').text
reviewers_num = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[3]/strong/em').text

writer.writerow([title, director, ratings_num, reviewers_num])
file.close()

