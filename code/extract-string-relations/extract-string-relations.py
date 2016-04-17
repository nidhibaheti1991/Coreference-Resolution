#coding=utf8
import sys
import string
#filePath = sys.argv[1]
#file = open(filePath,'r')
#data = file.read()
#lines = data.split('\n')
#print lines
#outputFile = open("output.txt","w+")
#outputFile.write(file.read())
#print file.read()

def extractHead(inputString , char1, char2):
	try:
		startIndex = inputString.index(char1) + 1
		endIndex = inputString.index(char2) + 1
		return inputString[startIndex:endIndex]
	except ValueError:
		return ""


string1 = '[<1,PN>एक धनी (सेठ)]'
string2 = '[<1,PRN>(उसके) बंगले]'
string3 = '[<1,PN>(सेठ)]'

print extractHead(string1,'(',')')==extractHead(string2,'(',')')

print extractHead(string1,'(',')') in string3





