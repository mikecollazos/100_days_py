import os
from bs4 import BeautifulSoup
import requests

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
# print(soup.title)
article_tags = soup.find_all("a", class_="storylink")

article_texts = []
article_links = []

for tag in article_tags:
    # print(tag.getText())
    article_texts.append(tag.getText())
    # print(tag.get("href"))
    article_links.append(tag.get('href'))
    #print('************************************************')


article_upvote = [int(upvote.string.split()[0]) for upvote in soup.find_all('span', class_='score')]

max_votes = max(article_upvote)
max_votes_index = article_upvote.index(max_votes)

print(article_texts[max_votes_index])
print(article_links[max_votes_index])
print(article_upvote[max_votes_index])




# print(article_upvote)

# try:
#     with open("website.html") as f:
#         contents = f.read()
#         #print(contents)
# except Exception as e:
#     print(e)

# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup.title.string)
# # print(soup.li.string)
# all_anchor_tags = soup.find_all(name="a")

# # for tag in all_anchor_tags:
# #     print(tag.getText())
# #     print(tag.get('href'))

# heading = soup.find(name="h1", id='name')
# print(heading)

# print(soup.find_all(name="p"))


# h3_heading = soup.find(name='h3', class_='heading')
# print(h3_heading.getText())


# company_url = soup.select_one(selector='p a')
# print(company_url)

# name = soup.select_one(selector='#name')
# print(name.get_text())

# headings = soup.select('.heading')
# print(headings)


