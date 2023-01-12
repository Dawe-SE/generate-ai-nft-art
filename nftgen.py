import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import requests, atexit, subprocess, random, ast, numpy, threading, random
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option("detach", True)
options.add_argument("--headless")
options.add_argument("--window-size=1400,600")
s = Service(ChromeDriverManager().install())




def worker(amount):
    for i in range(1, amount):
        try:
            driver = webdriver.Chrome(options=options, service=s)
            driver.get("https://app.wombo.art/")
            WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[3]/div/div/div[1]/div[1]/div[1]/div[1]/input')))
            driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[3]/div/div/div[1]/div[1]/div[1]/div[1]/input').send_keys("Rug")

            select_style = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[3]/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div').click()
            driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[3]/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div').click()

            driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div/img').click()
            time.sleep(2)
            click_create = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[3]/div/div/div/div[2]/div/button').click()
            print(str(threading.get_ident()) + " Generating image..\n")
            WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[3]/div/div/div[2]/div/p')))
            print(str(threading.get_ident()) + " Done generating image!\n")
            img = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[3]/div/div/div[2]/div/img')
            src = img.get_attribute('src')
            response = requests.get(src)
            with open(str(threading.get_ident()) + ".jpg", "wb") as f:
                f.write(response.content)

            img = Image.open(str(threading.get_ident()) + ".jpg")

            for x in range(440, 640):
                for y in range(1700, 1755):
                    img.putpixel((x, y), (18, 18, 18))

            stringOfAsciiAndNumbers = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
            filename= "".join(random.choices(stringOfAsciiAndNumbers, k=14))
            img.save(r'C:\Users\Administrator\Desktop\wombo\img\img' + filename + ".jpg", 'JPEG')
            os.remove(str(threading.get_ident()) + ".jpg")
            driver.close()
        except Exception as e:
            print(str(threading.get_ident()) + " Timeout error!\n")
            print(e)


threads = []
started = False
threadCount = 4
while not started:
    if 5000 % int(threadCount) == 0:
        amount_per_thread = 5000/int(threadCount)
        for i in range(0, threadCount):
            t = threading.Thread(target=worker, args=[int(amount_per_thread)])
            threads.append(t)
            t.start()
            print(i)

        started = True
    else:
        print("Not evenly divisible")

