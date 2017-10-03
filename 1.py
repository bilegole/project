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




def load_out(a):
	
	len98 = len(a)
	count = 0
	while (len(a)>(count+1)):
		if isinstance(a[count],list):
			random_test(a[count])
			count = count + 1
		else:
			while (count+1) < len98 :
				if a[count] != None :
					a[count].print_self()
				count = count + 1


#****************************************************************************
#此函数用于写入数据文件
#****************************************************************************

def write_file(class_t):
	content = []
	content.append('ev_in')
	if class_t.id_list != None:
		content.append('001@'+class_t.id_str[:3]+class_t.id_str[4:]+'\n')
		content.append('002@'+class_t.id_str[2:4]+'\n')
	if class_t.name != None :
		content.append('003@'+class_t.name+'\n')
	if class_t.teacher != None :
		content.append('004@'+class_t.teacher.iden+'\n')
	with open(class_t.id_list[-1], 'w+') as file:
		file.writelines(content)







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
		elif judge == '002':
			id_list.insert(2,string[4:])	 
			class_tmp.give_id(id_list)
		elif judge == '003':
			name_oc = ''
			name_oc = string[4:]
			class_tmp.give_name(name_oc)
		elif judge == '004':
			id_ot = ''
			id_ot = string[4:]
			class_tmp.give_teacher_id(id_ot)
	for j in range(len(id_list)):
		id_list[j] = int (id_list[j])
	rewrite(id_list,class_tmp)
#	DATEBASE[id_list[0]][id_list[1]][id_list[2]][id_list[3]][id_list[4]][id_list[5]] = class_tmp
#	class_tmp.print_self()

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


#此函数用于写入高维数组，并且使其指针正确
def rewrite(t,class_t):
	global DATEBASE	
	i_5 = copy.copy(DATEBASE[t[0]][t[1]][t[2]][t[3]][t[4]])
	i_4 = copy.copy(DATEBASE[t[0]][t[1]][t[2]][t[3]])
	i_3 = copy.copy(DATEBASE[t[0]][t[1]][t[2]])
	i_2 = copy.copy(DATEBASE[t[0]][t[1]])
	i_1 = copy.copy(DATEBASE[t[0]])
	i_5[t[5]] = class_t
	i_4[t[4]] = i_5
	i_3[t[3]] = i_4
	i_2[t[2]] = i_3
	i_1[t[1]] = i_2
	DATEBASE[t[0]] = i_1
#****************************************************************************
#这两个函数被用于测试数组
#****************************************************************************

#此函数用于测量数组维度
def mat_test(mat):
	dem = 1
	while isinstance(mat[0],list):
		print(len(mat))
		mat = mat[0]
		dem = dem + 1
	print('这是一个',dem,'维数组')

#此函数用于对数组中的每一个成员进行操作

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
					a[count].print_self()
				count = count + 1

#****************************************************************************
#以下是工具类函数的区域
#包括:将list转化为字符串的trans
#****************************************************************************


def trans (list_tmp):
	st = ''
	for i in list_tmp : 
		st = st + str(i)
	return st



#****************************************************************************
#以下是定义类的区域
#包括:课程，老师
#****************************************************************************






class Classt(object):
	def __init__(self):
                self.id_list = None
                self.id_str = None
                self.name = None
                self.teacher = None
                pass
	def give_id(self,id_list):
		self.id_list = id_list
		self.id_str = trans(self.id_list)
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
		print('list:',self.id_list)
		print('老师的id为',self.teacher.iden)
	def load_out(self,path):				#此函数需要date的目录（如：／Users/yuyang/project/date ）
		global HOME
		print('开始测试')
		print (os.path.abspath('.'))
		os.chdir(os.path.join(HOME,path))




		for count in range(len(self.id_list)-1):
			tip = False
			for dd in [x for x in os.listdir('.') if os.path.isdir(x)]:
				if str(self.id_list[count]) == dd :
					tip = True
					break
			print(os.listdir('.'))
			print (os.path.abspath('.'))
			if  tip == False :
				os.mkdir(os.path.join(os.path.abspath('.'),str(self.id_list[count])))
			print(os.listdir('.'))
			os.chdir(str(self.id_list[count]))



		#for count in range(len(self.id_list)-1):
		#	tip = False
		#	for dd in [x for x in os.listdir('.') if os.path.isdir(x)]:
		#		if self.id_list[count] == dd :
		#			tip = True
		#			break
		#	print(os.listdir('.'))
		#	if  tip == 1 :
		#		os.mkdir(os.path.join(os.path.abspath('.'),str(self.id_list[count])))
		#	print(os.listdir('.'))
		#	os.chdir(str(self.id_list[count]))









#		tip = False	
#		for dd in [x for x in os.listdir('.') if os.path.isdir(x)]
#			if self.id_list(-1) == dd :
#				tip = True
#				break
		write_file(self)




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

HOME = os.path.abspath('.')

DATEBASE = creat_datebase1(7,20,5,30,8,9)
#DATEBASE[1][1][4][1][1][1] = Classt()
read_in('date')
random_test(DATEBASE)
os.chdir(HOME)
print('程序执行完毕')		
ii_id = [1,1,3,1,1,1]
ii = Classt()
ii.give_id(ii_id)
ii.give_name('算法导论')
ii.give_teacher_id('teacher_id')
ii.print_self
ii.load_out('date')
#mat = [[[2,3],[3,5]],[[4,5],[4,2]]]
#mat_test(DATEBASE)
