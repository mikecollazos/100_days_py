import os
import requests
from bs4 import BeautifulSoup


script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

year = input('Which Year do you want to travel to? Type the date in this format YYYY-MM-DD: \n')

URL=f'https://www.billboard.com/charts/hot-100/{year}'

response = requests.get(URL)


soup = BeautifulSoup(response.text, 'html.parser')
#all_songs = soup.find_all('h3', id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
all_songs = soup.select("li ul li h3")

all_songs = [song.text.strip() for song in all_songs]

