
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

OLLAMA_URL = "http://localhost:11434/api/chat"

# task = "Лесенкой называется набор кубиков, в котором каждый более верхний слой содержит кубиков меньше, чем предыдущий. Требуется написать программу, вычисляющую число лесенок, которое можно построить из N кубиков.\nВходные данные\nВо входном файле INPUT.TXT записано натуральное число N (1 ≤ N ≤ 100) – количество кубиков в лесенке.\n\nВыходные данные\nВ выходной файл OUTPUT.TXT необходимо вывести число лесенок, которые можно построить из N кубиков."

with open("task1.json", "r") as file:
    tasks = file.read()

data=json.dumps({
    "model": "deepseek/deepseek-r1-distill-llama-70b:free",
    "messages": [
        {
            "role": "user",
            "content": """
Реши задачу:
Требуется сложить два целых числа А и В.

Входные данные
В единственной строке входного файла INPUT.TXT записаны два натуральных числа через пробел. 
Значения чисел не превышают 109.
 
Выходные данные
В единственную строку выходного файла OUTPUT.TXT нужно вывести одно целое число — сумму чисел А и В.
Верни только законченный скрипт на Python. Используй конструкцию if __name__ == '__main__': для обработки ввода и вывода."""
        }
        # {
        #     "role": "assistant",
        #     "content": f"Hi"
        # },
        # {
        #     "role": "user",
        #     "content": f"How are you doing?"
        # }
    ],
})

headers={
    "Authorization": "",
    "Content-Type": "application/json"
}

response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, data=data)

response.raise_for_status()

print(response.json()["choices"][0]["message"]["content"])


# select_d = Select()

# select_d.select_by_value()

# Реши задачу:
# Требуется сложить два целых числа А и В.

# Входные данные
# В единственной строке входного файла INPUT.TXT записаны два натуральных числа через пробел. 
# Значения чисел не превышают 109.
 
# Выходные данные
# В единственную строку выходного файла OUTPUT.TXT нужно вывести одно целое число — сумму чисел А и В.

# Напиши законченный скрипт на Golang. Используй package main, import необходимые пакеты. Используй стандартный ввод и вывод вместо файлов.



# Реши задачу:
# Требуется сложить два целых числа А и В.
# Входные данные
# В единственной строке входного файла INPUT.TXT записаны два натуральных числа через пробел. 
# Значения чисел не превышают 109.
 
# Выходные данные
# В единственную строку выходного файла OUTPUT.TXT нужно вывести одно целое число — сумму чисел А и В.
# Напиши законченный скрипт на Python. Используй конструкцию if __name__ == '__main__': для обработки ввода и вывода.

