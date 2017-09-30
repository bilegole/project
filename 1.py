#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os






def read_parameter():
	pass
#	par_0 = [9,8,30,5,20,7]
#	bundle = [par_0]
#	if os.path.exists('./parameter.cof'):	
#		with open('./parameter.cof', 'r') as file:
#    			par_1 =file.read()
#			bundle = process(par_1,bundle)
#	return bundle

def read_in(dir):
	dir = str(dir)
	now = os.path.abspath('.')
	then = os.path.join(now,dir)
	os.chdir(then)
	dir_1 = [x for x in os.listdir('.') if x !='.DS_Store' ]	
	len98 = len (dir_1)
	count = 0
	while (count<len(dir_1)):
		if os.path.isdir(dir_1[count]):
			read_in(dir_1[count])
			count = count + 1
			os.chdir(then)
		else:
			load_in_test(dir_1[count])					
			count = count +1
def load_in_test(a) :
	with open(a, 'w') as f:
		f.write('完成检测')




def creat_datebase1(*need):
	need = list(need)
	mat = None
	bundle = [need,mat]
	while len(bundle[0]) > 0 :
		bundle1 = creat_datebase2(bundle[0],bundle[1])
		bundle=bundle1
	return bundle[1]
	
def creat_datebase2(need,mat=0):
	mat1 = []
	while need[0] > 0 :
		mat1.append(mat)
		need[0] = need[0] -1
	need.pop(0)
	bundle = [need , mat1]
	return bundle


def mat_test(mat):
	dem = 1
	while isinstance(mat[0],list):
		mat = mat[0]
		dem = dem + 1
	print('这是一个',dem,'维数组')


def random_test(a):
	
	len98 = len(a)
	count = 0
	while (len(a)>(count+1)):
		if isinstance(a[count],list):
			random_test(a[count])
			count = count + 1
		else:
			while (count+1) < len98 :
				a[count]=5
				count = count + 1

class classt():
	def __init__(self):
		pass
	def init():
		pass	
		
	def get_inf_from_file():
		pass
	def save_inf_into_file():
		pass
		
class teacher():
	def __init__(self):
		pass


date = (10,8,30,4,20,7)





def main():
	bundle = read_parameter()
	creat_datebase(9,8,30,5,20,7)
	read_in()

building = {'A':1,'B':2,'C':3,'D':4,'E':5,'信远楼':6,'工训中心':7,'大学生活动室':8,'北操场':9,'南操场':10}
department = {'计算机':1,'通信工程':2,'电子工程':3,'机电工程':4,'物理与光电工程':5,'软件':6,'网络与信息安全':7,'微电子':8,'生命科学与技术':9,'先进材料与纳米技术':10,'数学与统计':11,'空间科学与技术':12,'外国语':13,'经济与管理':14,'人文':15,'马克思主义':16,'国际教育':17,'网络与技术教育':18,'体育部':19}


#_______test area_______________________________________________________________________
#dir = []
#for i in dir=read_in():
print ("*************************************************************************")
print ("*************************************************************************")
print ("*************************************************************************")
print ("*************************************************************************")
read_in('1')
#______________________________________________________________________________








#s = 'test.text'


#with open(s,'a+') as f :
#		f.write(s)
