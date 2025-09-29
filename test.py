
import requests

OLLAMA_URL = "http://localhost:11434/api/chat"

task = "Лесенкой называется набор кубиков, в котором каждый более верхний слой содержит кубиков меньше, чем предыдущий. Требуется написать программу, вычисляющую число лесенок, которое можно построить из N кубиков.\nВходные данные\nВо входном файле INPUT.TXT записано натуральное число N (1 ≤ N ≤ 100) – количество кубиков в лесенке.\n\nВыходные данные\nВ выходной файл OUTPUT.TXT необходимо вывести число лесенок, которые можно построить из N кубиков."

payload = {
    "model": "deepseek-coder:33b",
    "messages": [
        {
            "role": "system",
            "content": "You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek          \nCompany, and you only answer questions related to computer science. For politically sensitive           \nquestions, security and privacy issues, and other non-computer science questions, you will refuse to    \nanswer."
        },
        {
            "role": "user",
            "content": f"Реши задачу на python: {task}"
        }
    ],
    "stream": False,
    "options": {
        "temperature": 0.2,
        "num_predict": 2048
    }
}

response = requests.post(OLLAMA_URL, json=payload)
response.raise_for_status()  # Проверка на ошибки HTTP

result = response.json()
print(result["message"]["content"])