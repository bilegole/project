#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

#去掉tab值


#def rm_tab(los):
#	for string in los :
#		if string[:2] ==
	
file_in = 'for_test'

#with open(file_in, 'r') as file:
#	out = []
#	buffer_in = file.readlines()
#	for string in buffer_in :
#		#print ('+++++++++++++++++++++++++++++++++++++')
#		#print(string)
#		while string[:1] =='\t' or string[:1]==' ' :
#			string = string[1:]
#		#print(string)
#		if string[-1:] == '\n':
#			string = string[:-1]
#		if string != "":
#			print(string)
#	###	for letter in string:
#	###		print (letter)
#	###	
#        ###
#        ###



#这是一个读取，将其每一行内容去掉结尾的\n后的非空拼成list作为返回值
def read_file(file,path = os.path.abspath('.')):
	file_path = os.path.join(path,file)
	with open(file_path, 'r') as file:
		buffer_in = file.readlines()
#	out = []
#	for string in buffer_in:
#		string = rm_tail(string)
#		out.append(rm_tail(string))	
#	return buffer_in

#	return [result for string in buffer_in if result = cl_str(string)]
	return [cl_str(string) for string in buffer_in if cl_str(string) != '' ]
#去掉行末
def cl_str(string):
	while string[:1] =='\t' or string[:1]==' ' :
		string = string[1:]
	if string[-1:] == '\n':
		string = string[:-1]
	return string

a= read_file(file_in)
print (a)
#print(read_file(file_in))
map(print,a)
