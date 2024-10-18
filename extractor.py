# extractor.py
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def extract_comments(video_url):
    driver_path = 'N:/data science/projects/sentiment analysis/chromedriver-win64/chromedriver.exe'
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)

    driver.get(video_url)
    time.sleep(5)

    body = driver.find_element(By.TAG_NAME, 'body')
    for _ in range(30):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)

    comments = driver.find_elements(
        By.CSS_SELECTOR, 'span.yt-core-attributed-string.yt-core-attributed-string--white-space-pre-wrap'
    )
    comment_list = [comment.text.strip() for comment in comments]

    driver.quit()

    # Save to CSV
    df = pd.DataFrame(comment_list, columns=['Comment'])
    df.to_csv('youtube_comments.csv', index=False)
    print("Comments saved to youtube_comments.csv")
