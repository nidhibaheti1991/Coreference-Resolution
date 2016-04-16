from bs4 import BeautifulSoup
import urllib
r = urllib.urlopen('http://www.bharatdarshan.co.nz/magazine/literature/23/usne-kaha-tha.html').read()
soup = BeautifulSoup(r,"html.parser")
#print soup.get_text()
file = open("parseddata.txt", "wb")
for para in soup.find_all('span'):
    print  para.get_text().encode('utf-8')
    file.write("NEW PARAGRAPH"+para.get_text().encode('utf-8')+"\n")

file.flush()
file.close()
