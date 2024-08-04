from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import os
import re


path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(executable_path=path))

url = "https://freecodecamp.org/"
driver.get(url)


get_domain = re.search(r"^(http://|https://)((?:\w+\.)*(?:\w+))/$", url)

pages = []


# Locating Landing Page
time.sleep(0.5)
urls = driver.find_elements(By.TAG_NAME, "a")


def link_finder(link):
    time.sleep(0.5)
    driver.get(link)
    links = driver.find_elements(By.TAG_NAME, "a")
    return [link.get_attribute("href") for link in links]


# Get Link from Parent
for link in urls:
    if link.get_attribute("href") not in pages and re.search(f"^(http://|https://)(?:\w+\.)*{get_domain.group(2)}/", link.get_attribute("href"), re.IGNORECASE):
        pages.append(link.get_attribute("href"))


lists = []

for page in pages:
    lists.append(link_finder(page))

result = []
result.extend(pages)

for links in lists:
    for link in links:
        if link not in result and link and re.search(f"^(http://|https://)(?:\w+\.)*{get_domain.group(2)}/", link, re.IGNORECASE):
            result.append(link)


with open("links.txt", "w+") as file:
    for link in sorted(result):
        file.write(link)
        file.write("\n")




# driver.save_screenshot("/screenshots/main.png")

# # scrap Index
# page = driver.page_source

# #create folder if not exists
# try:
#     directory = f'templates/{url.replace("http://", "").replace(".","_")}'
#     os.makedirs(directory)
# except:
#     pass

# # create and write index.html
# with open(f"{directory}/index.html", "w+") as file:
#     file.write(page)

# # Getting CSS links
# WebDriverWait(driver, 10).until(
#     ec.presence_of_all_elements_located((By.TAG_NAME, "link"))
# )
# links = driver.find_elements(By.TAG_NAME, "link")

# urls = []

# for link in links:
#     urls.append(str(link.get_attribute("href")))



# # (http://qwndirect.com/)(uns/assets/css/)(bootstrap.min.css)
# #           1                   2                   3
# # create CSS folders and files
# for link in urls:
#     time.sleep(1)
#     driver.get(link)
#     if verified := re.search(f"^({url})((?:\w+\/)*)((?:(?:\w+\.)*css)?)$", link):
#         try: os.makedirs(f"{directory}/{verified.group(2)}")
#         except: pass
#         with open(f"{directory}/{verified.group(2)}/{verified.group(3)}", "w+") as file:
#             file.write(driver.page_source)


# time.sleep(10)
