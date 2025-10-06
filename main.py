from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time
import requests
import json

load_dotenv("config.env")

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

        paragraphs = driver.find_elements(By.CSS_SELECTOR, "p.text")

        # for i in paragraphs:
        #     print(i.text)
    finally:
        print()
    return [i.text for i in paragraphs]

key_id = 0
def generate_code(task):
    # payload = {
    #     "model": "deepseek-coder:6.7b-instruct-q4_K_M",
    #     "messages": [
    #         {
    #             "role": "system",
    #             "content": "You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek          \nCompany, and you only answer questions related to computer science. For politically sensitive           \nquestions, security and privacy issues, and other non-computer science questions, you will refuse to    \nanswer."
    #         },
    #         {
    #             "role": "user",
    #             "content": f"Реши задачу на python, сделай ввод из файла INPUT.TXT, а вывод в файл OUTPUT.TXT и в ответ верни только код самого решения: {task}"
    #         }
    #     ],
    #     "stream": False,
    #     "options": {
    #         "temperature": 0.2,
    #         "num_predict": 2048
    #     }
    # }
    
    global key_id

    data=json.dumps({
        "model": "deepseek/deepseek-chat-v3.1:free",
        "messages": [
            {
                "role": "user",
                "content": 
f"""Ты — опытный программист, решающий олимпиадные задачи. Твоя задача — проанализировать предложенную проблему и предоставить только готовый код на Python без каких-либо пояснений, комментариев или примеров использования.

Алгоритм работы:
1. Внимательно проанализируй задачу и определи класс сложности.
2. Продумай алгоритм решения, учитывая ограничения.
3. Выбери оптимальные структуры данных.
4. Убедись, что решение эффективно и проходит по времени.
5. Напиши код.

Требования к коду:
- Используй стандартный ввод/вывод (input/print).
- Не используй функции, если это не необходимо для структуры.
- Учитывай все крайние случаи.
- Код должен быть готов к компиляции и работе.

Задача:
{task}
"""
            }
        ]
    })
    
    try:
        st_code = 429
        st_code_cnt = 0
        while st_code == 429:
            headers={
                "Authorization": KEYS[key_id],
                "Content-Type": "application/json"
            }
            
            response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, data=data)
            st_code = response.status_code
            print(st_code)
            if st_code == 429:
                st_code_cnt += 1
                if st_code_cnt >= 10:
                    key_id += 1
                    st_code_cnt = 0
                    if key_id == len(KEYS):
                        exit(0)
                time.sleep(10)

        response.raise_for_status()
        
        result = response.json()
        return result["choices"][0]["message"]["content"]    #["message"]["content"] #["response"]
        
    except requests.exceptions.RequestException as e:
        return f"Ошибка запроса: {e}"
    except KeyError:
        return "Ошибка: неверный формат ответа от сервера"

def upload_with_selenium(driver, task_id):
    #driver = webdriver.Chrome()  # или другой браузер
    
    try:
        folder_path = "solutions"
        files = os.listdir(folder_path)
        py_files = [f for f in files if f.endswith('.py')]
        py_files = sorted(py_files)
        
        # iter = 0
        # for fi in py_files:
        #     task_id = int(fi.replace(".py", ""))
        url = f"https://acmp.ru/index.asp?main=task&id_task={task_id}"
        driver.get(url)
        
        print(f"{task_id} - iter")

        textarea = driver.find_element(By.ID, "fname")
        textarea.clear()
        textarea.send_keys(os.path.abspath(f"solutions/{task_id}.py"))
        
        submit_btn = driver.find_element(By.XPATH, "//input[@type='button' and @value='Отправить']")
        submit_btn.click()
        
        time.sleep(15)
    except:
        time.sleep(100)
    # finally:
    #     driver.quit()

#upload_with_selenium()

options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome()

login(driver)

#upload_with_selenium(driver)

start_id = 0
with open(f"last_task_id.lst", "r") as file:
    start_id = int(file.read())

excepted = ""
with open(f"excepted.lst", "r") as file:
    excepted = file.read()

print(len(KEYS))

except_list = [int(i) for i in excepted.split(" ")]
for task_id in range(start_id, 1001):
    if task_id not in except_list:
        try:
            print(f"Current task is {task_id}")
            task_text = parse_task(driver, task_id)

            task_text.insert(-2, "\nВходные данные\n")
            task_text.insert(-1, "\nВыходные данные\n")

            code = generate_code("".join(task_text))

            if "```" in code:
                code = code.split("```python")[1]
                code = code.split("```")[0]
            
            with open(f"solutions/{task_id}.py", "w") as file:
                file.write(code)

            # time.sleep(10)
            # upload_with_selenium(driver, task_id)
            # time.sleep(10)
            # os.system("sudo sync && echo 3 | sudo tee /proc/sys/vm/drop_caches")
            # os.system("free -h")
            # time.sleep(10)

            upload_with_selenium(driver, task_id)

        finally:
            with open(f"last_task_id.lst", "w") as file:
                file.write(str(task_id))
            print(f"Task {task_id} is completed")
