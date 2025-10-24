import requests
from bs4 import BeautifulSoup

html = requests.get("https://naver.com").text
soup = BeautifulSoup(html, "html.parser")

for link in soup.find_all("a"):
    print(link.get("href"))
