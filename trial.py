from bs4 import BeautifulSoup
import requests


Url = "https://www.classcentral.com"
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
page = requests.get(Url, headers = agent)
content = page.content
soup = BeautifulSoup(content, 'lxml')
box  = soup.find('page-home', class_ = "content-page")


with open('index.html' , 'w', encoding = 'utf-8') as file:
    file.write(soup.prettify())



images = soup.find_all('img', class_ = 'width-100 radius-small')
resolvedURLs = []

for image in images:
 src = image.get('src')
 resolvedURLs.append(requests.compat.urljoin(Url, src))

for image in resolvedURLs:
 webs = requests.get(image)
 open('images/' + image.split('/')[-1], 'wb').write(webs.content)

