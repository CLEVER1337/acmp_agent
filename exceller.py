from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import csv
import uuid

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

data = []
tasks_examples = []

try:
    for id in range(1, 1001):
        task_id = uuid.uuid4()

        name, info, text, examples = parse_task(driver, id)

        for i in range(len(examples)):
            examples[i]["id"] = i
            examples[i]["task_id"] = task_id
            tasks_examples.append(examples)

        task = {
            "id" : task_id,
            "num": id,
            "complexity" : info.split(": ")[-1].replace(")", ""),
            "name" : name,
            "description" : ''.join(text[:-2]),
            "time": info.split(": ")[1].replace(". Память", ""),
            "memory": info.split(": ")[2].replace(" Сложность", "")
        }

        data.append(task)

        print(f"{id} parsed\n")
finally:
    with open("tasks.csv", "w", encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(data[0].keys())

        for i in data:
            writer.writerow(i.values())
    
    with open("examples.csv", "w", encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(tasks_examples[0].keys())

        for i in tasks_examples:
            writer.writerow(i.values())
