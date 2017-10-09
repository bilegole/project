#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import copy

#****************************************************************************
#这是用于创建高维数组的函数
#****************************************************************************


#以下两个函数用于建立DATEBASE所需的高维数组
def creat_datebase1(*need):
	need_1 = list(copy.copy(need))
	for e in range(len(need)):
		need_1[e] = need[-(e+1)]
		
	need = list(need)
	mat = None
	bundle = [need,mat]
	while len(bundle[0]) > 0 :
		bundle1 = creat_datebase2(bundle[0],bundle[1])
		bundle=bundle1
	return bundle[1]
	
def creat_datebase2(need,mat=0):
	mat1 = []
	while need[-1] > 0 :
		mat1.append(mat)
		need[-1] = need[-1] -1
	need.pop(-1)
	bundle = [need , mat1]
	return bundle


#这是对数据库中内存的操作，主要是解决python3不变量内存相同，变量内存指同的问题
def dat_ch(list_id,content,datebase):
    #list_id指数据的位置id（list形式）,content指要插入的内容,datebase指要更改的数据库，最好是直通原数组
    list_len = len(list_id)
    list_cp = copy.copy(list_id)
    for j in range(len(list_cp)):
        list_cp[j] = int (list_cp[j])
    i_list = []
    for i in range(len(list_id)):
        i_list.append(0)
        if i == 0 :
            i_list[i] = copy.copy(datebase[list_cp[0]])
            datebase[list_cp[0]] = i_list[i]
        elif i == len(list_id)-1  :
            i_list[i-1][list_cp[i]] = content
        else :
            i_list[i] = copy.copy(i_list[i-1][list_cp[i]])
            i_list[i-1][list_cp[i]] = i_list[i]


#此函数未开始写
#@@@\\\
def rewrite_chart():
	pass		

#这是DATEBASE自检函数，输出每个被赋值的课堂
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
#读取文本形式存放的数据库
#****************************************************************************

#调用每一个文本数据
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
#将其写入到内存中
def read_file_in(file_in):
	#print ('开始read——in——函数')
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
	#print(buffer_in)
	for i in range(len(buffer_in)) :

		string =  buffer_in[i]
		judge = string[:3]
		if judge == '001':
			for letter in string[4:-1]:
				id_list.append(letter)
		elif judge == '002':
			id_list.insert(2,string[4:-1])	 
			class_tmp.give_id(id_list)
		elif judge == '003':
			name_oc = string[4:-1]
			class_tmp.give_name(name_oc)
		elif judge == '004':
			na_ot = string[4:-1]
			class_tmp.give_teacher_str(na_ot)
	dat_ch(id_list,class_tmp,DATEBASE)
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
		elif a[count] != None :
			a[count].print_self()
			a[count].load_out('date')
		else:
			pass
		count = count + 1

#****************************************************************************
#以下是工具类函数的区域
#包括:将list转化为字符串的trans
#****************************************************************************


def trans (list_tmp):
	st = ''
	for i in list_tmp : 
		t = str (i)
		st = st + t
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
		self.score = None
		self.must = None
		self.time = None
#		self.tea_dict = None
#	目前有6位，最大大小分别为：9,8,30,5,20,7
#	储存在文本中时，以：
#	001@abefg
#	002@cb
#	形式存在
	def give_id(self,id_list):
		self.id_list = id_list
		self.id_str = trans(self.id_list)
		print(id_list)
	def give_name(self,name):
                 self.name = name
	def give_teacher_str(self,st):
                self.teacher = st
	#	self.tea_dict = read_str(self.teacher)
		#self.tea_id = iden
	def print_self(self):
		print('类classt已创建')
		print('课程名称为：',self.name)
		print('id为',self.id_str)
		print('list:',self.id_list)
		print('老师的名字为：',self.teacher)
	#此函数需要date的目录（如：／Users/yuyang/project/date ）
	def load_out(self,path):			
		global HOME
		os.chdir(os.path.join(HOME,path))
		for count in range(len(self.id_list)-1):
			tip = False
			for dd in [x for x in os.listdir('.') if os.path.isdir(x)]:
				if str(self.id_list[count]) == dd :
					tip = True
					break
			if  tip == False :
				os.mkdir(os.path.join(os.path.abspath('.'),str(self.id_list[count])))
			os.chdir(str(self.id_list[count]))
		self.write_file()
	def write_file(self):
		content = []
		content.append('ev_in\n')
		if self.id_list != None:
			content.append('001@'+self.id_str[:2]+self.id_str[4:]+'\n')
			content.append('002@'+self.id_str[2:4]+'\n')
		if self.name != None :
			content.append('003@'+self.name+'\n')
		if self.teacher != None :
			content.append('004@'+self.teacher+'\n')
		with open(str(self.id_list[-1]), 'w+') as file:
			file.writelines(content)

#这里有个问题，要输入的是course_t的id，却输入了老师的字符串
	def course_out(self):
		tmp = course_t()
		tmp.in_id(cla_to_cou(self))
		tmp.in_tea(read_str(self.teacher))
		tmp.in_score(self.score)
		tmp.in_must(self.must)
		tmp.in_time(self.time)	
		return tmp
	#返回一个course_t类型数据



def read_str(str):
	pass
def cla_to_cou(cls):
	return result		#此处返回用于从classt中生成的course_t的id	



class Chartt(object):
	def __init__(self):
		self.department = None		#指这张课表所属学院
		self.major = None		#指这张课表所属专业
		self.class_n = None		#指这张课表所属班级
	#	self.week = None		#指这张课表所属星期
		self.mat = None			#这张表所需数据库
						#1.星期几 2.课次 3.周 
						#1.7	  2.5	 3.20 	
	def setup(self):
		self.datebase = creat_datebase1(7,5,20)
		













#
#class teacher(object):
#	def __init__(self,iden):
#	        self.iden = iden
#		self.post = None		
#		self.name = None
#	def id_in(self)

#教师编码
#




date = (10,8,30,4,20,7)

class course_t():
	def __init__(self):
		self.id_list = None			#这是指list形式的id
		self.id_str = None			#这是指string形式的id
		self.tea_list = []			#这是指老师的列表
		self.tea_num = len(self.tea_list)	#这是指老师的数量
		self.score = None			#这是指course_t的学分
		self.must = None			#这是指course_t是否为必修课
		self.time = None			#这是指course_t的学时
	def in_id(self,lst):
		self.id_list = lst
		self.id_str = trans(self.id_list)	
	def in_tea():
		pass
	def in_score(self,num):
		self.score = num
	def in_must(self,must):
		self.must = must
	def in_time(self,time):
		pass
#课程编码
#校区：1:南校区	2:北校区0:特殊	
#周几：（1-7）星期几
#课次：1:1-2	2:3-4	3:5-6	4:7-8	0:晚自修
#教室：同DATEBASE编码
#楼层：1-8
#教室：0-30








def main():
#	HOME = os.path.abspath('.')
#	DATEBASE = creat_datebase1(9,8,30,5,20,7)
#	read_in('date')
#	random_test(DATEBASE)
#	os.chdir(HOME)
#	print('程序执行完毕')		
	pass

building = {'A':1,'B':2,'C':3,'D':4,'E':5,'信远楼':6,'工训中心':7,'大学生活动室':8,'北操场':9,'南操场':10}
department = {'计算机':1,'通信工程':2,'电子工程':3,'机电工程':4,'物理与光电工程':5,'软件':6,'网络与信息安全':7,'微电子':8,'生命科学与技术':9,'先进材料与纳米技术':10,'数学与统计':11,'空间科学与技术':12,'外国语':13,'经济与管理':14,'人文':15,'马克思主义':16,'国际教育':17,'网络与技术教育':18,'体育部':19}


#_______test area_______________________________________________________________________
#dir = []
#for i in dir=read_in():
#read_in('1')
#______________________________________________________________________________




HOME = os.path.abspath('.')
DATEBASE = creat_datebase1(9,8,30,5,20,7)
read_in('date')
random_test(DATEBASE)
os.chdir(HOME)
print('程序执行完毕')		
ii_id = ['1','1','01','1','1','1']
ii = Classt()
print('aaa')
ii.give_id(ii_id)
print('bbb')
ii.give_name('算法导论')
print ('ccc')
ii.give_teacher_str('teacher')
print (ii.name)
ii.print_self()
ii.load_out('date')
#mat = [[[2,3],[3,5]],[[4,5],[4,2]]]
#mat_test(DATEBASE)
