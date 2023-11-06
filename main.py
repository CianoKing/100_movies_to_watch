import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
empire_webpage = response.content

soup = BeautifulSoup(empire_webpage, "html.parser")
item_list = soup.find_all(name="h3", class_="title")

for _ in range(len(item_list)-1, -1, -1):
    movie = item_list[_].getText()
    with open("movies.txt", mode="a") as movie_file:
        movie_file.write(f"{movie}\n")
