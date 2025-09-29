from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time
import requests
import json

load_dotenv("config.env")

KEYS = os.getenv("DEEPSEEK_KEYS").split(",")

print(KEYS)
