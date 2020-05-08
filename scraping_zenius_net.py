import requests
from bs4 import BeautifulSoup as bs
page = requests.get('https://www.zenius.net/blog/')
page = bs(page.content,'html.parser')
next_page_link = page.find(class_='next page-numbers').get('href')
titles, authors, descs, dates, links = [],[],[],[],[]
#for i in range(4):	
while True:
	articles = page.find_all('article')
	for data in articles:
		titles.append(data.find(class_='entry-title').get_text())
		authors.append(data.find('em').get_text())
		descs.append(data.find(class_='entry-summary').find('p').get_text())
		dates.append(data.find('time','published').get_text().strip())
		links.append(data.find(class_='entry-title').find('a').get('href'))
	if page.find(class_='next page-numbers') != None: 
		next_page_link = page.find(class_='next page-numbers').get('href')
	else:
		break
	page = bs(requests.get(next_page_link).content,'html.parser')

for i in range(len(titles)):
	print('title : ',titles[i])
	print('author : ',authors[i])
	print('date : ',dates[i])
	print('description : ',descs[i])
	print('link : ',links[i])
	print('\n\n')

print("oke")
