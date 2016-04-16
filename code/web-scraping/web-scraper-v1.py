from bs4 import BeautifulSoup
import urllib
num=0
with open('web-address-v1.txt', 'r') as f_in:
	modelLines = f_in.read()
	addr = modelLines.split('\n')
	for webAddr in addr:
		num = num+1
		print "Hello"+webAddr
		r = urllib.urlopen(webAddr).read()
		soup = BeautifulSoup(r,"html.parser")
		outputFile = open("Story"+str(num)+".txt","w+")
		for para in soup.find_all('td', class_="body-text"):
			outputFile.write(para.get_text().encode('utf-8')+"\n")
		outputFile.flush()	
		outputFile.close()
