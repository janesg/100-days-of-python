from bs4 import BeautifulSoup
# import lxml

with open("./website.html", encoding="UTF-8") as file:
    soup = BeautifulSoup(file, features="html.parser")
    # soup = BeautifulSoup(contents, features="lxml")

print(soup.prettify())
print(f"{soup.title.name} : {soup.title.string}")
print(soup.find_all(name="a")[1].get_text())
print(soup.find_all(name="a")[1].get("href"))

# Equivalent
print(soup.find(id="name").get_text())
print(soup.select(selector="#name")[0].get_text())

# Equivalent
print(soup.find_all(class_="heading"))
print(soup.select(".heading"))

print(soup.select_one(selector="p a").get_text())
