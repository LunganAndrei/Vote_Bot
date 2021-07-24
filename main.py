from selenium import webdriver
import os
import time

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")  # don t open a window
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-shm-usage")
count =0
while True:
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)
    driver.get("https://aerotim.ro/")

    alege_destinatia=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[1]/button")
    alege_dublin=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[3]/div[1]/form/div/ul/li[3]/input")
    vote=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[3]/div[1]/form/div/p[1]/input")
    alege_destinatia.click()
    time.sleep(2)
    alege_dublin.click()
    time.sleep(2)
    vote.click()
    time.sleep(10)
    count +=1
    print(count)





# cod to run BOT_AIRPORT>heroku run python main.py