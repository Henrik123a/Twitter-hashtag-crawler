from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random
import time

# Initializes selenium and webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def twitter(start_link, i=1):
    if i >= 7:
        return

    #Loads twitter url
    driver.get('https://twitter.com/search?q=%23' + start_link)
    #waits for content to load
    time.sleep(5)
    #finds all hastags on the page and puts them in a list
    tag = driver.find_elements(By.XPATH, '//a[contains(@href, "hashtag/")]')
    try:
        rantag = tag[random.randrange(0,len(tag)-1)].text[1:]  # choses a random hastag
    except:
        print('feil, prøv med ny start_link')
    print(str(f'{i}: {rantag}'))  #prints hashtag
    return twitter(rantag, i+1)

twitter("Winter")
driver.close()


