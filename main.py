import requests
from bs4 import BeautifulSoup as bs

git_username = input("Type Username :")

url = 'https://github.com/' + git_username

r = requests.get(url)

soup = bs(r.content, 'html.parser')

profile_img = soup.find('img', {'alt': 'Avatar'})['src']

print(profile_img)
