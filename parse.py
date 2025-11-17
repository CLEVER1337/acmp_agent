from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import json
import requests
import time

load_dotenv("config.env")
#Mistral
LOGIN = os.getenv("ACMP_LOGIN")
PASSWORD = os.getenv("ACMP_PASSWORD")

KEYS = os.getenv("DEEPSEEK_KEYS").split(",")

def login(driver):
    print("Выполняем авторизацию...")
    driver.get("https://acmp.ru/index.asp?main=login")
    
    login_field = driver.find_element(By.NAME, "lgn")
    password_field = driver.find_element(By.NAME, "password")
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Ok']")
    
    login_field.clear()
    login_field.send_keys(LOGIN)
    password_field.clear()
    password_field.send_keys(PASSWORD)
    
    submit_button.click()

    time.sleep(3)

def parse_task(driver, task_id):
    try:
        url = f"https://acmp.ru/index.asp?main=task&id_task={task_id}"
        driver.get(url)

        name = driver.find_elements(By.CSS_SELECTOR, "h1")
        info = driver.find_elements(By.CSS_SELECTOR, "i")
        text = driver.find_elements(By.CSS_SELECTOR, "p.text")
        examples = driver.find_elements(By.CSS_SELECTOR, "td.table-example__data")
        examples_text = []
        for i in range(0, len(examples), 2):
            examples_text.append({
                "input": examples[i].get_attribute("data-example"),
                "output": examples[i + 1].get_attribute("data-example")
            })

    except:
        print("Eror while parsing occured!\n")
    finally:
        return name[0].text, info[0].text, [i.text for i in text], examples_text

options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome()

login(driver)

driver.get("https://acmp.ru/index.asp?main=task&id_task=999")

b = driver.find_element(By.XPATH, "//select[@name='lang']")

select = Select(b)

select.select_by_value("GO")

time.sleep(1000)

# b = driver.find_elements(By.XPATH, "//tr[@class='lightgreen']")

# print(b[0].find_elements(By.TAG_NAME, "td")[5].find_element(By.TAG_NAME, "span").get_attribute("class"))

#print(b.text)

# g = driver.find_element(By.XPATH, "//tr[@class='lightgreen']/td/span[@class='green']")
# print(g.text)

# b = driver.find_element(By.XPATH, "//tr[@class='lightgreen']/td/span[@class='black']")
# print(b.text)

# for i in a:
#     if i.get_attribute("href") == "https://acmp.ru/?main=user&id=547596" or i.get_attribute("href") == "/?main=user&id=547596":
#         try:
#             par = i.find_element(By.XPATH, "//td/span[@class='green']")
#             print(par.text)
#         except:
#             pass

#         try:
#             par = i.find_element(By.XPATH, "//td/span[@class='red']")
#             print(par.text)
#             continue
#         except:
#             pass
        # try:
        #     gr = par.find_elements(By.CLASS_NAME, "green")
        #     print(gr[0].text)
        # except:
        #     print("green error")

        # try:
        #     red = par.find_elements(By.CLASS_NAME, "red")
        #     print(red[0].text)
        # except:
        #     print("red error")



#time.sleep(10000)

# data = []

# try:
#     for id in range(1, 1001):
#         name, info, text, examples = parse_task(driver, id)

#         task = {
#             "id" : id,
#             "complexity" : info.split(": ")[-1].replace(")", ""),
#             "name" : name,
#             "description" : ''.join(text[:-2]),
#             "examples": examples,
#             "time": info.split(": ")[1].replace(". Память", ""),
#             "memory": info.split(": ")[2].replace(" Сложность", "")
#         }

#         data.append(task)

#         print(f"{id} parsed\n")
# finally:
#     with open("tasks.json", "w") as file:
#         file.write(json.dumps(data))
