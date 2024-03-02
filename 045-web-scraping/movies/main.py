import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)

soup = BeautifulSoup(response.text, features="html.parser")
titles = [title.get_text() for title in soup.select("h3.title")]

with open("./movies.txt", encoding="UTF-8", mode="w") as file:
    for idx in reversed(range(len(titles))):
        file.write(f"{titles[idx]}\n")
