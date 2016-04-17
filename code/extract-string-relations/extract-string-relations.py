#coding=utf8
import sys
import string


def isHeadEqual(inputStr1,inputStr2):
	try:
		char1 = '('
		char2 = ')'
		startIndex = inputStr1.index(char1) + 1
		endIndex = inputStr1.index(char2) 
		head1 = inputStr1[startIndex:endIndex]
		startIndex = inputStr2.index(char1) + 1
		endIndex = inputStr2.index(char2) 
		head2 = inputStr2[startIndex:endIndex]
		return head1==head2
	except ValueError:
		return False




def isSubstring(inputStr1,inputStr2):
	try:
		char1 = '('
		char2 = ')'
		startIndex = inputStr1.index(char1) + 1
		endIndex = inputStr1.index(char2) 
		head1 = inputStr1[startIndex:endIndex]
		startIndex = inputStr2.index(char1) + 1
		endIndex = inputStr2.index(char2) 
		head2 = inputStr2[startIndex:endIndex]
		return head1 in inputStr2 or head2 in inputStr1
	except ValueError:
		return False
	

# Test Cases
#string1 = '[<1,PN>एक धनी (सेठ)]'
#string2 = '[<1,PRN>(उसके) बंगले]'
#string3 = '[<1,PN>(सेठ)]'


#print isHeadEqual(string1,string2)
#print isHeadEqual(string1,string3)
#print isHeadEqual(string2,string3)
#print isSubstring(string1,string2)
#print isSubstring(string1,string3)
#print isSubstring(string2,string3)






