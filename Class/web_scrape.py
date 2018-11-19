import requests as r
from bs4 import BeautifulSoup as b
import inflection as i

url = r.get('http://www.dailysmarty.com/topics/python')
soup = b(url.text,'html.parser')

words = []
for link in soup.find_all('a'):
    words.append((link.get('href')))

posts = []
for item in words:
    if "posts/" in item:
        posts.append(item)

for item in posts:
    new = i.titleize(item)
    final = new.replace("/Posts/", '')
    print(final)

#Jordan's solution
# def title_generator(links):
#     titles = []

#     def post_formatter(url):
#         if 'posts' in url:
#             url = url.split('/')[-1]#Good use of split here, where he grabs the second half of what is being split. 
#             url = url.replace('-', ' ')
#             url = titleize(url)
#             titles.append(url)


#     for link in links:
#         post_formatter(link["href"])


#     return titles


# req = r.get('http://www.dailysmarty.com/topics/python')
# soup = b(req.text, 'html.parser')
# links = soup.find_all('a')
# titles = title_generator(links)

# for title in titles:
#     print(title)
# print(links)