#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import copy
#去掉tab值


#def rm_tab(los):
#	for string in los :
#		if string[:2] ==
	
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



#这是一个读取，将其每一行内容去掉开头的tab和空格，以及结尾的\n后的非空拼成list作为返回值
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




#这是写入函数，name表示写入文件的名字，content(list)表示要写入的内容，path(可选)表示文件所在路径，mode表示模式(0:覆盖，1:追加)
def write_file(name,content,path = os.path.abspath('.'),mode = 0):
	with open(os.path.join(path,name),"w") as f:
		f.writelines(map(pro_for_out,map(rm_blank,content)))


def pro_for_out(string):
	return string+'\n'

#这是用于去除list中的空白项
def rm_blank(list_t):
	list_a = copy.copy(list_t)
	for count in range(len(list_t)):
		accumlate = 0
		if list_t[count] == '':
			accumulate = accumulate + 1
			list_a.pop(count-accumulate)
	return	list_a
#*****************************************************************************************************************
#这是专为这次工作写的函数

def select_class(line):
	if line[:58]!='<span><a class ="a22" href="../../../../html/kebiao/2017b/':
		return ''
	else:
		line_1 = line[58:]
		count=0
		for letter in line_1:
			count = count + 1
			if  letter == 'x' :
				return line_1[:count-1]
		


#*****************************************************************************************************************
#*****************************************************************************************************************

file_in = 'for_test'
file_out = 'tmp'

#*****************************************************************************************************************
#*****************************************************************************************************************
#a= read_file(file_in)
#a = map(select_class,a)
#print(read_file(file_in))
#write_file('tmp',a)

words = ['测试开始\n','\n','测试结束\n']
for word1 in words:
	print(word1)
t = words.pop(1)
for word in t:
	print (word,end = '')
#print(t)










