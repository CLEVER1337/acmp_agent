from selenium import webdriver
from selenium.webdriver.common.by import By
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

excepted = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 50 51 52 54 55 56 58 59 60 61 62 63 64 65 66 67 68 69 71 72 74 75 79 81 82 83 84 85 86 87 88 89 92 93 94 95 96 97 98 99 100 102 103 106 108 109 113 114 115 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 138 140 141 142 143 144 145 146 147 148 149 150 151 153 154 156 157 158 159 160 163 164 165 167 170 171 172 173 178 180 181 183 185 188 189 190 192 195 196 198 199 200 202 203 205 206 207 208 209 211 213 214 215 216 218 219 224 225 228 231 233 234 235 236 237 243 245 249 250 253 255 257 258 260 262 263 264 265 266 267 269 270 271 272 273 274 275 276 277 278 279 281 282 283 284 286 287 288 289 290 291 292 293 294 295 296 297 298 299 301 303 304 305 308 309 311 312 314 315 316 317 318 319 320 321 323 324 325 326 327 328 329 330 331 332 333 335 336 338 340 342 345 347 348 349 350 352 354 355 357 361 364 367 368 369 370 374 375 376 377 380 381 384 385 387 388 390 392 393 394 395 400 401 411 412 413 416 422 424 425 427 430 431 432 439 440 441 442 447 449 452 455 457 460 461 462 463 465 466 471 475 477 479 481 482 488 491 493 494 495 496 498 499 501 504 506 508 509 510 513 514 515 516 517 518 519 520 521 522 523 524 525 529 531 534 535 539 542 543 544 548 549 550 554 556 564 574 576 578 580 581 582 590 596 597 598 600 601 605 606 628 629 633 634 637 638 639 641 642 643 648 649 653 664 665 670 675 676 678 679 681 682 684 685 686 687 688 689 691 692 693 694 695 696 697 698 699 700 701 703 710 711 712 715 726 728 729 733 742 743 745 754 755 756 757 758 759 760 762 763 764 765 766 773 777 778 780 782 784 785 790 791 792 793 803 811 813 814 815 816 817 818 819 820 822 826 831 833 836 838 839 841 842 843 844 845 846 848 854 858 859 869 871 872 876 890 892 894 895 897 899 903 904 905 906 907 908 913 916 923 924 925 933 935 936 938 939 940 941 942 944 945 946 947 948 950 952 955 957 961 966 967 970 975 978 984 996 997"

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

def upload_with_selenium(driver, task_id):
    #driver = webdriver.Chrome()  # или другой браузер
    
    try:
        folder_path = "solutions"
        files = os.listdir(folder_path)
        py_files = [f for f in files if f.endswith('.go')]
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

driver = webdriver.Chrome()

login(driver)

link = driver.find_element(By.LINK_TEXT, "Мои задачи")
link.click()

solved = driver.find_elements(By.CSS_SELECTOR, "p.text")[0].text

print([int(i) for i in solved.split(" ")])

time.sleep(1000)
