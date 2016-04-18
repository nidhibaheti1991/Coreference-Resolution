import requests
import io
from bs4 import BeautifulSoup

iter_url=open('web-addresses-v2.txt','r')
list_of_urls=iter_url.read().split(',\n')
iter_url.close()
count=0
for url in list_of_urls:
	print url
	r = requests.get(url)

	soup= BeautifulSoup(r.content,"html.parser")

	links = soup.find_all("a")

	g_data=soup.find_all("div",{"class":"post hentry"})

	for item in g_data:
		with io.open("stories_v2/file_"+str(count)+".txt","w",encoding='utf-8') as f:
			f.write(item.contents[3].text)
			f.write(item.contents[7].text)
		count=count+1
