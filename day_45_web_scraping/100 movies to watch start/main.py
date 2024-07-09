import os
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

response = requests.get(URL)
movie_web_page = response.text

soup = BeautifulSoup(movie_web_page, 'html.parser')
all_titles = soup.find_all('h3', class_="title")
all_titles.reverse()

for title in all_titles:
    print(title.text)


try:
    with open("movie.txt", 'w') as f:
        for title in all_titles:
            f.write(title.text)
            f.write("\n")
except Exception as e:
    print(e)