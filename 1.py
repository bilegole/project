#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import copy





def read_file(file):
	with open(a, 'w') as f:
                f.readlines()










#	par_0 = [9,8,30,5,20,7]
#	bundle = [par_0]		
#	if os.path.exists('./parameter.cof'):	
#		with open('./parameter.cof', 'r') as file:
#    			par_1 =file.read()
#			bundle = process(par_1,bundle)
#	return bundle






#****************************************************************************
#此函数用于打开被输入文件夹下的所有文件
#****************************************************************************
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
			read_file_in(os.path.join(os.path.abspath('.'),dir_1[count]))
		count = count  + 1

#****************************************************************************
#此函数用于读取文件（课）的配置
#****************************************************************************
def read_file_in(file_in):
	global DATEBASE
	ev_in = 'ev_in'
	ev_conf = 'ev_conf'
	ev_out = 'ev_out'
	with open(file_in, 'r') as file:
	        buffer_in = file.readlines()
	title = buffer_in[0][:-1]
	buffer_in.pop(0)
	id_list = []
	class_tmp = Classt()
	for i in range(len(buffer_in)) :
		string =  buffer_in[i][:-1]
		judge = string[:3]
		if judge == '001':
			for letter in buffer_in[i][4:-1]:
				id_list.append(letter)
			#print(id_list)
		elif judge == '002':
			id_list.insert(2,string[4:])	 
			#print(id_list)
			class_tmp.give_id(id_list)
			#print('iii')
		elif judge == '003':
			name_oc = ''
			name_oc == string[4:]
			class_tmp.give_name(name_oc)
		elif judge == '004':
			id_ot = ''
			id_ot = string[4:]
			class_tmp.give_teacher_id(id_ot)
	for j in range(len(id_list)):
		id_list[j] = int (id_list[j])
	print (id_list)	
	rewrite(id_list,class_tmp)
#	DATEBASE[id_list[0]][id_list[1]][id_list[2]][id_list[3]][id_list[4]][id_list[5]] = class_tmp
#	class_tmp.print_self()

#重写吧
#def read_file_in(buffer_in) :
#	#parameter = ['001','002','003']
#	global DATEBASE
#	a = buffer_in [1]
#	b = buffer_in [2]
#	print ('ttt')
#	if a[:3] == '001':    
##			001是后面跟的是课程编号，用于在程序中定位（防止换算过程中出bug） 
##			001@11111
##			002后面跟的是教室层编号，因为有两位，所以最好特殊处理
##			002@11
#		buffer_ini = buffer_in 
#		b = b[4:6]
##	喝了太多酒，调不了了。。。。。。。。
##	妈勒个鸡的
#		buffer_ini.insert(2,b)
#		t = trans ( a[4:9] ) 
#		class_tmp = classt()
#		print(buffer_ini)
#		class_tmp.give_id(t)
#		print(buffer_ini)
#		buffer_ini.pop(0)
#		buffer_ini.pop(0)
#		buffer_ini.pop(0)
#		for p in buffer_ini:
#			p_tmp = p[:3]
#			p_tmp2= p[4:]
#			if p_tmp == '003':
#				class_tmp.give_name(p_tmp2)
#	#			003用于写入课程的名字。
#			if p_tmp == '004':
#				class_tmp.give_teacher_id(p_tmp2)
#	#			004 用于写入老师编号
#		#class_tmp.print_self()	
#	DATEBASE[t[0]][t[1]][t[2]][t[3]][t[4]][5] = class_tmp
def trans(a):
	t = []
	for i in a :
		t.append(i)
	return t
#****************************************************************************
#这是用于创建高维数组的函数
#****************************************************************************
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

def rewrite(t,class_t):
	global DATEBASE	
	i_5 = copy.copy(DATEBASE[t[0]][t[1]][t[2]][t[3]][t[4]])
	i_4 = copy.copy(DATEBASE[t[0]][t[1]][t[2]][t[3]])
	i_3 = copy.copy(DATEBASE[t[0]][t[1]][t[2]])
	i_2 = copy.copy(DATEBASE[t[0]][t[1]])
	i_1 = copy.copy(DATEBASE[t[0]])
	print (t[5])
	i_5[t[5]] = class_t
	i_4[t[4]] = i_5
	i_3[t[3]] = i_4
	i_2[t[2]] = i_3
	i_1[t[1]] = i_2
	DATEBASE[t[0]] = i_1
#****************************************************************************
#这两个函数被用于测试数组
#****************************************************************************
def mat_test(mat):
	dem = 1
	while isinstance(mat[0],list):
		print(len(mat))
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
				if a[count] != None :
					print (a[count])
					a[count].print_self()
				count = count + 1


#****************************************************************************
#以下是工具类函数的区域
#包括:将list转化为字符串的trans
#****************************************************************************


def trans (list_tmp):
	st = ''
	for i in list_tmp : 
		st = st + i
	return st



#****************************************************************************
#以下是定义类的区域
#包括:课程，老师
#****************************************************************************






class Classt(object):
	def __init__(self):
                self.id = None
                self.id_str = None
                self.name = None
                self.teacher = None
                pass
	def give_id(self,id_list):
		self.id = id_list
		self.id_str = trans(self.id)
#		print(self.id)
#		print(self.id_str)
	def give_name(self,name):
                 self.name = name
	def give_teacher_id(self,iden):
                self.teacher = teacher(iden)
		#self.tea_id = iden
	def print_self(self):
		print('类classt已创建')
		print('课程名称为：',self.name)
		print('id为',self.id_str)
		print('list:',self.id)
		print('老师的id为',self.teacher.iden)

class teacher(object):
	def __init__(self,iden):
	        self.iden = iden

date = (10,8,30,4,20,7)












def main():
	pass

building = {'A':1,'B':2,'C':3,'D':4,'E':5,'信远楼':6,'工训中心':7,'大学生活动室':8,'北操场':9,'南操场':10}
department = {'计算机':1,'通信工程':2,'电子工程':3,'机电工程':4,'物理与光电工程':5,'软件':6,'网络与信息安全':7,'微电子':8,'生命科学与技术':9,'先进材料与纳米技术':10,'数学与统计':11,'空间科学与技术':12,'外国语':13,'经济与管理':14,'人文':15,'马克思主义':16,'国际教育':17,'网络与技术教育':18,'体育部':19}


#_______test area_______________________________________________________________________
#dir = []
#for i in dir=read_in():
#read_in('1')
#______________________________________________________________________________


#现在在调试数组的空间大小，程序总是说数组越界。。。。。
#去他妈的

#bundle = read_parameter()




DATEBASE = creat_datebase1(7,20,5,30,8,9)
#DATEBASE[1][1][4][1][1][1] = Classt()
read_in('date')
random_test(DATEBASE)
print('程序执行完毕')		

#mat = [[[2,3],[3,5]],[[4,5],[4,2]]]
#mat_test(DATEBASE)
