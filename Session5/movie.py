from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import csv
import re

#공백제거 함수
def no_space(text):
    text1 = re.sub('&nbsp; | &nbsp;| \n|\t|\r', '', text)
    text2 = re.sub('\n\n', '', text1)
    return text2

#디버깅 모드
# chrome_options = Options()
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = './chromedriver'
driver = webdriver.Chrome(chrome_driver)

# 원래 이렇게 하면 됨!!
# 근데 폴더에 chromedriver파일 가져다놓기
# 글구 그냥 터미널에 python movie.py 로 실행

#실행할 웹페이지 불러오기
driver.get("https://movie.naver.com/")

rankbtn = driver.find_element(By.XPATH, '//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
rankbtn.click()
time.sleep(1)

rank_page = driver.page_source


soup = BeautifulSoup(rank_page, 'html.parser')
rankings = soup.select('div.tit3')

#csv 생성
file = open('movie.csv', mode="w", newline='')
writer = csv.writer(file)
writer.writerow(["rank", "title", "outline", "director", "rating"])


for rank, ranking in enumerate(rankings, start=1):
    title = ranking.select_one('a')['title']
    if rank <= 10:
        titlebtn = driver.find_element(By.XPATH, f'//*[@id="old_content"]/table/tbody/tr[{rank}+1]/td[2]/div/a')
    else :
        titlebtn = driver.find_element(By.XPATH, f'//*[@id="old_content"]/table/tbody/tr[{rank}+2]/td[2]/div/a')
    titlebtn.click()
    time.sleep(1)
    info_page = driver.page_source
    soup = BeautifulSoup(info_page, 'html.parser')
    outline_tmp = soup.select_one('dl.info_spec > dd > p').get_text()
    #개요 공백 제거
    outline = no_space(outline_tmp)
    director = soup.select_one('dl.info_spec > dd > p > a').get_text()
    #별점 있는지 없는지 판단
    rating_tmp = soup.select_one('#actualPointPersentBasic > div.star_score > span.st_off > span.st_on')
    if rating_tmp is not None:
        rating_tmp = rating_tmp.get_text()
        rating = re.findall(r'\d+\.\d+', rating_tmp)
        rating = rating[0]

    else:
        rating = None
    
    writer.writerow([rank, title, outline, director, rating])

    if rank >= 20:
        break
    rankbtn = driver.find_element(By.XPATH, '//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
    rankbtn.click()
    time.sleep(1)


driver.quit()
file.close()









