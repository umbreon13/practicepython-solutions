import requests
from bs4 import BeautifulSoup

#1
# base_url = 'http://www.nytimes.com'
# r = requests.get(base_url)
# soup = BeautifulSoup(r.text, features="html.parser") 
# for story_heading in soup.find_all(class_="story-heading"): 
#     if story_heading.a: 
#         print(story_heading.a.text.replace("\n", " ").strip())
#     else: 
#         print(story_heading.contents[0].strip())

#2
# base_url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
# r = requests.get(base_url)
# soup = BeautifulSoup(r.text, features="html.parser")
# all_p_cn_text_body = soup.select("div.parbase.cn_text > div.body > p")
# for elem in all_p_cn_text_body[7:]:
#   print(elem.text)

#3
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, features="html.parser") 
for story_heading in soup.find_all(class_="indicate-hover css-vf1hbp"): 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())
# <h3 class="indicate-hover css-vf1hbp">Nobody Knows Why the New Weight Loss Drugs Work</h3>