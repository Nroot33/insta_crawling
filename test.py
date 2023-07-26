from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import re
import time
import pandas as pd
from datetime import datetime


def select_first(driver):
    first = driver.find_element(By.CSS_SELECTOR, "div._aagw")
    first.click()
    time.sleep(3)


def get_content(driver):
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    content = soup.select('div._a9zs')[0].text
    tags = re.findall(r'#[^\s#,\\]+', content)
    date = soup.select('time._aaqe')[0]['datetime'][:10]
    like = soup.select('section._ae5m._ae5n._ae5o')[0].findAll('span')[-1].text
    instaid = driver.find_element(By.CSS_SELECTOR, "div.xt0psk2").text
    url = driver.current_url
    # try:

    # except:
    # content = ""
    # tags = ''
    # date = ''
    # like = 0
    data = [instaid, content, date, like, tags, url]
    return data
    # return url


def move_next(driver):
    try:
        right = driver.find_element(By.CSS_SELECTOR, "div._aaqg._aaqh")
        right.click()
        time.sleep(10)
    except:
        results_df = pd.DataFrame(results)

        results_df.columns = ["instaid", "content",
                              "date", "like", "tags", "url"]
        results_df.to_csv('./insta_crawling1-1.csv', index=False)


driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')
time.sleep(15)


def insta_search(word):
    url = 'https://www.instagram.com/explore/tags/' + word
    return url


url = insta_search('thewall포토콘테스트')
driver.get(url)


time.sleep(10)

select_first(driver)

results = []


target = 600

for i in range(target):
    try:
        data = get_content(driver)
        results.append(data)
        move_next(driver)
    except:
        time.sleep(10)
        move_next(driver)
    time.sleep(10)


# print(results)

results_df = pd.DataFrame(results)

results_df.columns = ["instaid", "content", "date", "like", "tags", "url"]
results_df.to_csv('./insta_crawling1.csv', index=False)
