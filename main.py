from selenium import webdriver
import os
import time

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")  # don t open a window
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)
count =0
while True:

    driver.get("https://aerotim.ro/")
    alege_destinatia=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[1]/button")
    time.sleep(2)
    alege_dublin=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[3]/div[1]/form/div/ul/li[3]/input")
    time.sleep(2)
    vote=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[3]/div[1]/form/div/p[1]/input")
    time.sleep(2)
    alege_destinatia.click()
    time.sleep(2)
    alege_dublin.click()
    time.sleep(2)
    vote.click()
    count += 1
    print(count)
    time.sleep(3)






# cod to run BOT_AIRPORT>heroku run python main.py