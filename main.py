from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv
import os
import time
import requests
import json

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

def get_solved_tasks(driver: webdriver.Chrome):
    link = driver.find_element(By.LINK_TEXT, "Мои задачи")
    link.click()

    solved = driver.find_elements(By.CSS_SELECTOR, "p.text")[0].text

    return [int(i) for i in solved.split(" ")]

def parse_task(driver: webdriver.Chrome, task_id):
    try:
        url = f"https://acmp.ru/index.asp?main=task&id_task={task_id}"
        driver.get(url)

        paragraphs = driver.find_elements(By.CSS_SELECTOR, "p.text")

        texts = [i.text for i in paragraphs]

        if "Пояснение" in [i.text for i in driver.find_elements(By.TAG_NAME, "h2")]:
            texts.pop()

        texts.insert(-2, "\nВходные данные\n")
        texts.insert(-1, "\nВыходные данные\n")

        texts.append("\nПримеры:\n")
        examples = driver.find_elements(By.CSS_SELECTOR, "td.table-example__data")
        examples_text = []
        for i in range(0, len(examples), 2):
            texts.append(f"Пример номер {i}:\n")
            texts.append(f"Input: {examples[i].get_attribute('data-example')}\n")
            texts.append(f"Output: {examples[i + 1].get_attribute('data-example')}\n\n")
        
    finally:
        print()
    return "".join(texts)

def translate_task(task, key_id):
    data=json.dumps({
        "model": "deepseek/deepseek-r1-0528-qwen3-8b:free",
        "messages": [
            {
                "role": "user",
                "content": f"Переведи на английский, верни только перевод: \"{task}\""
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
        #print(result)
        return result["choices"][0]["message"]["content"]
        
    except requests.exceptions.RequestException as e:
        return f"Ошибка запроса: {e}"
    except KeyError:
        return "Ошибка: неверный формат ответа от сервера"

def select_lang(lang="PY"):
    b = driver.find_element(By.XPATH, "//select[@name='lang']")

    select = Select(b)

    select.select_by_value(lang)

def clean_code(code):
    if "<think>" in code:
        code = code.split("</think>")[1]

    if "```python" in code:
        code = code.split("```python")[1]
    elif "```go" in code:
        code = code.split("```go")[1]
    return code.split("```")[0]

key_id = 0
def nn_generate_code(prompt):
    global key_id

    data=json.dumps({
        "model": "minimax/minimax-m2:free",
        "messages": [
            {
                "role": "user",
                "content": prompt
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
            
            response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, data=data, timeout=1200)

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
        #print("\n\n\n")
        #print(result["choices"][0]["message"]["content"]) #434
        return clean_code(result["choices"][0]["message"]["content"])#, translated_task    #["message"]["content"] #["response"]
        
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return None
    except KeyError:
        print("Ошибка: неверный формат ответа от сервера")
        return None

def generate_code(task, lang="py"):
    try:
        code = None
        if lang == "py":
            code = nn_generate_code(
                prompt=f"""
Реши задачу, верни только код:

{task}

Верни только законченный скрипт на Python. Используй конструкцию if __name__ == '__main__': для обработки ввода и вывода. Return only final code."""
            )
        elif lang == "go":
            code = nn_generate_code(
                prompt=f"""
Реши задачу, верни только код:

{task}

Верни только законченный скрипт на Golang. Используй package main, import необходимые пакеты. Используй стандартный ввод и вывод вместо файлов. Return only final code."""
            )
        
        return code
    
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return None
    except KeyError:
        print("Ошибка: неверный формат ответа от сервера")

def regenerate_code(task, code_old, error, lang="py"):
    try:
        code = None
        if lang == "py":
            code = nn_generate_code(
                prompt=f"""
Есть задача:

{task}

Эта задача была решена следукющим кодом:

{code_old}

Но этот код вызвал ошибку {error}

Помоги исправить ошибку и верни только законченный скрипт на Python. Используй конструкцию if __name__ == '__main__': для обработки ввода и вывода. Return only final code."""
            )
        elif lang == "go":
            code = nn_generate_code(
                prompt=f"""
Есть задача:

{task}

Эта задача была решена следукющим кодом:

{code_old}

Но этот код вызвал ошибку {error}

Помоги исправить ошибку и верни только законченный скрипт на Golang. Используй package main, import необходимые пакеты. Используй стандартный ввод и вывод вместо файлов. Return only final code."""
            )
        
        return code
    
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return None
    except KeyError:
        print("Ошибка: неверный формат ответа от сервера")

def upload_with_selenium(driver, task_id, lang="py"):
    #driver = webdriver.Chrome()  # или другой браузер
    
    try:
        url = f"https://acmp.ru/index.asp?main=task&id_task={task_id}"
        driver.get(url)
        
        #print(f"{task_id} - iter")

        textarea = driver.find_element(By.ID, "fname")
        textarea.clear()
        if lang == "py":
            textarea.send_keys(os.path.abspath(f"solutions/{task_id}.py"))
        elif lang == "go":
            textarea.send_keys(os.path.abspath(f"solutions/{task_id}.go"))
        
        submit_btn = driver.find_element(By.XPATH, "//input[@type='button' and @value='Отправить']")
        submit_btn.click()
        
        time.sleep(15)
    except:
        time.sleep(100)
    # finally:
    #     driver.quit()

#upload_with_selenium()

def check_task_status(driver: webdriver.Chrome):
    while True:
        driver.get("https://acmp.ru/index.asp?main=status")

        try:
            lg = driver.find_elements(By.XPATH, "//tr[@class='lightgreen']")

            print(lg[0].find_elements(By.TAG_NAME, "td")[5].find_element(By.TAG_NAME, "span").get_attribute("class"))
            if lg[0].find_elements(By.TAG_NAME, "td")[5].find_element(By.TAG_NAME, "span").get_attribute("class") == "black":
                time.sleep(10)
                continue
            elif lg[0].find_elements(By.TAG_NAME, "td")[5].find_element(By.TAG_NAME, "span").get_attribute("class") == "green":
                return "Ok"
            else:
                return lg[0].find_elements(By.TAG_NAME, "td")[5].find_element(By.TAG_NAME, "span").text
        except:
            continue


options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome()

login(driver)

#upload_with_selenium(driver)

excepted = get_solved_tasks(driver)

print(f"Already solved are these tasks: {excepted}\n\n\n")

for task_id in range(1, 1001):
    if task_id not in excepted:
        print(f"Current task is {task_id}")
        try:
            code = None
            task_text = parse_task(driver, task_id)
            
            select_lang("PY")

            while code == None:
                code = generate_code(task_text, "py")
                
            with open(f"solutions/{task_id}.py", "w") as file:
                file.write(code)

            upload_with_selenium(driver, task_id)
            status = check_task_status(driver)

            if status != "Ok":
                task_text = parse_task(driver, task_id)
                
                select_lang("PY")

                while True:
                    code = regenerate_code(task_text, code, status, "py")
                    if code != None:
                        break
                    
                with open(f"solutions/{task_id}.py", "w") as file:
                    file.write(code)

                upload_with_selenium(driver, task_id)
                status = check_task_status(driver)

                if status != "Ok":
                    task_text = parse_task(driver, task_id)
            
                    select_lang("GO")

                    while True:
                        code = generate_code(task_text, "go")
                        if code != None:
                            break
                        
                    with open(f"solutions/{task_id}.go", "w") as file:
                        file.write(code)

                    upload_with_selenium(driver, task_id, "go")
                    status = check_task_status(driver)

                    if status != "Ok":
                        task_text = parse_task(driver, task_id)
                        
                        select_lang("GO")

                        while True:
                            code = regenerate_code(task_text, code, status, "go")
                            if code != None:
                                break
                            
                        with open(f"solutions/{task_id}.go", "w") as file:
                            file.write(code)

                        upload_with_selenium(driver, task_id, "go")
                        status = check_task_status(driver)

        finally:
            print(f"Task {task_id} is completed, maybe not solved, but completed")
# TODO
# Context
# English prompts
# AnyLLM Mozilla
# Clean code
# json task_id result - reference for last code done? error

# SOEMHOW IT STOPPED WORKING WITH PYTHON
