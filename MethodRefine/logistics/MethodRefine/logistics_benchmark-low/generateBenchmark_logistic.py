# generateBenchmark.py
# coding=utf-8
# author=zhoujl
#！/usr/bin/python 
import time
import datetime
import random
import os



#创建文件

def generate_training_and_validating(training_path, validating_path, number_bottom, number_up, city, pkg_bottom, pkg_up, plane):


	for index in range(number_bottom, number_up + 1):
		city_num = city + 1
		pack_num = random.randint(pkg_bottom, pkg_up)
		plane_num = plane + 1
		car_num = city_num
		order_str = "["
		for i in range(0, pack_num - 1):
			order = [i, i + 1]
			order_str = order_str + str(order) + ","
		order_str = order_str + "]"

		ft = open(training_path + "training_" + str(index) + ".py", "w")
		fv = open(validating_path + "validating_" + str(index) + ".py", "w")
		#写进py文件的每一行 
		loc_py = 'state0.loc = {'
		load_py = 'state0.load = {'
		plane_num_py = 'state0.plane_nums = ' + str(plane_num-1) + "\n"
		declare_types = 'new_tihtn_planner.declare_types({'
		declare_funs = "new_tihtn_planner.declare_funs({load_plane:['pkg', 'location', 'plane'],load_truck:['pkg', 'location', 'truck'],by_plane:['plane', 'location'],drive_truck:['truck', 'location'], unload_truck:['pkg', 'location', 'truck'],unload_plane:['pkg', 'location', 'plane']})\n"
		instance = 'new_tihtn_planner.instance()\n'
		pyhop = "def execute(completable):\n\treturn new_tihtn_planner.pyhop(completable, allow, state0,["



		#生成location
		locList = list()
		declare_types = declare_types + "'location':["
		for i in  range(1, city_num):
			locList.append('loc(city'+str(i)+'_1).\n')
			locList.append('loc(city'+str(i)+'_2).\n')
			declare_types = declare_types + "('city" + str(i) + "','loc1'),"
			declare_types = declare_types + "('city" + str(i) + "','loc2'),"
		declare_types = declare_types + "],"


		#生成truck
		declare_types = declare_types + "'truck':["
		truckList = list()
		seen = set()
		for i in range(1, car_num):
			truckList.append('truck(truck'+str(i)+').\n')
			x = random.randint(1,city_num-1)
			y = random.randint(1,2)
		#生成truck初始位置
			loc_py = loc_py + "'truck"+ str(i) + "':('city" +str(i) + "','loc" + str(y) + "'),"
			load_py = load_py +  "'truck"+ str(i) + "':False,"
			declare_types = declare_types + "'truck" + str(i) + "',"
		#判断卡车覆盖了哪些城市
			seen.add(i)
		declare_types = declare_types + "],"


		#生成plane
		planeList = list()
		declare_types = declare_types + "'plane':["
		for i in range(1, plane_num):
			planeList.append('plane(plane' +str(i)+ ').\n')
			x = random.randint(1,city_num-1)
			#生成plane初始位置
			loc_py = loc_py + "'plane"+ str(i) + "':('city" +str(x) + "','loc1'),"
			load_py = load_py +  "'plane"+ str(i) + "':False,"
			declare_types = declare_types + "'plane" + str(i) + "',"
		declare_types = declare_types + "],"


		#生成package
		packageList = list()
		declare_types = declare_types + "'pkg':["
		for i in  range(1, pack_num + 1):
			packageList.append('package(pkg'+str(i)+').\n')
			x = random.randint(1,city_num-1)
			y = random.randint(1,2)
		#生成package初始位置
			loc_py = loc_py + "'pkg"+ str(i) + "':('city" +str(x) + "','loc" + str(y) + "'),"
			declare_types = declare_types + "'pkg" + str(i) + "',"

		#生成package目标位置
			x1 = random.randint(1,city_num-1)
			y1 = random.randint(1,2)
			while (x1 == x and y1 == y):
				x1 = random.randint(1,city_num-1)
				y1 = random.randint(1,2)
			pyhop = pyhop + "('delievery','pkg" + str(i) + "',('city" + str(x1) + "','loc" + str(y1) + "')),"
		pyhop  = pyhop + "]," + order_str + ", 9)\n"
		declare_types = declare_types + "]})\n"
		loc_py = loc_py + "}\n"
		load_py = load_py + "}\n"

		ft.writelines("#!/usr/bin/env python\n# coding=utf-8\nimport sys  \nsys.path.insert(0, './') \nfrom logistic import *\nimport new_tihtn_planner\n")
		ft.writelines('state0 = new_tihtn_planner.State(\'state0\')\n\n')
		ft.writelines("allow = True\n")
		ft.writelines(loc_py)
		ft.writelines(load_py)
		ft.writelines(plane_num_py)
		ft.writelines(declare_types)
		ft.writelines(declare_funs)
		ft.writelines(instance)
		ft.writelines(pyhop)
		ft.close()
		fv.writelines("#!/usr/bin/env python\n# coding=utf-8\nimport sys  \nsys.path.insert(0, './') \nfrom logistic import *\nimport new_tihtn_planner\n")
		fv.writelines('state0 = new_tihtn_planner.State(\'state0\')\n\n')
		fv.writelines("allow = False\n")
		fv.writelines(loc_py)
		fv.writelines(load_py)
		fv.writelines(plane_num_py)
		fv.writelines(declare_types)
		fv.writelines(declare_funs)
		fv.writelines(instance)
		fv.writelines(pyhop)
		fv.writelines("def add_methods(fun_obj_list):\n\tfor fun in fun_obj_list:\n\t\tnew_tihtn_planner.add_method(fun.func_name.split('__')[0], fun)\ndef reverse_methods():\n\tnew_tihtn_planner.reverse_methods()")
		fv.close()

def generate_testing(testing_path,number_bottom, number_up, city, pkg_bottom, pkg_up, plane):


	for index in range(number_bottom, number_up + 1):


		city_num = city + 1
		pack_num = random.randint(pkg_bottom, pkg_up)
		plane_num = plane + 1
		car_num = city_num

		order_str = "["
		for i in range(0, pack_num - 1):
			order = [i, i + 1]
			order_str = order_str + str(order) + ","
		order_str = order_str + "]"

		f = open(testing_path + "testing_" + str(index) + ".py", "w")
		#写进py文件的每一行 
		loc_py = 'state0.loc = {'
		load_py = 'state0.load = {'
		plane_num_py = 'state0.plane_nums = ' + str(plane_num-1) + "\n"
		declare_types = 'new_tihtn_planner.declare_types({'
		declare_funs = "new_tihtn_planner.declare_funs({load_plane:['pkg', 'location', 'plane'],load_truck:['pkg', 'location', 'truck'],by_plane:['plane', 'location'],drive_truck:['truck', 'location'], unload_truck:['pkg', 'location', 'truck'],unload_plane:['pkg', 'location', 'plane']})\n"
		instance = 'new_tihtn_planner.instance()\n'
		pyhop = "def execute(completable):\n\treturn new_tihtn_planner.pyhop(completable, allow, state0,["



		#生成location
		locList = list()
		declare_types = declare_types + "'location':["
		for i in  range(1, city_num):
			locList.append('loc(city'+str(i)+'_1).\n')
			locList.append('loc(city'+str(i)+'_2).\n')
			declare_types = declare_types + "('city" + str(i) + "','loc1'),"
			declare_types = declare_types + "('city" + str(i) + "','loc2'),"
		declare_types = declare_types + "],"


		#生成truck
		declare_types = declare_types + "'truck':["
		truckList = list()
		seen = set()
		for i in range(1, car_num):
			truckList.append('truck(truck'+str(i)+').\n')
			x = random.randint(1,city_num-1)
			y = random.randint(1,2)
		#生成truck初始位置
			loc_py = loc_py + "'truck"+ str(i) + "':('city" +str(i) + "','loc" + str(y) + "'),"
			load_py = load_py +  "'truck"+ str(i) + "':False,"
			declare_types = declare_types + "'truck" + str(i) + "',"
		#判断卡车覆盖了哪些城市
			seen.add(i)
		declare_types = declare_types + "],"


		#生成plane
		planeList = list()
		declare_types = declare_types + "'plane':["
		for i in range(1, plane_num):
			planeList.append('plane(plane' +str(i)+ ').\n')
			x = random.randint(1,city_num-1)
			#生成plane初始位置
			loc_py = loc_py + "'plane"+ str(i) + "':('city" +str(x) + "','loc1'),"
			load_py = load_py +  "'plane"+ str(i) + "':False,"
			declare_types = declare_types + "'plane" + str(i) + "',"
		declare_types = declare_types + "],"


		#生成package
		packageList = list()
		declare_types = declare_types + "'pkg':["
		for i in  range(1, pack_num + 1):
			packageList.append('package(pkg'+str(i)+').\n')
			x = random.randint(1,city_num-1)
			y = random.randint(1,2)
		#生成package初始位置
			loc_py = loc_py + "'pkg"+ str(i) + "':('city" +str(x) + "','loc" + str(y) + "'),"
			declare_types = declare_types + "'pkg" + str(i) + "',"

		#生成package目标位置
			x1 = random.randint(1,city_num-1)
			y1 = random.randint(1,2)
			while (x1 == x and y1 == y):
				x1 = random.randint(1,city_num-1)
				y1 = random.randint(1,2)
			pyhop = pyhop + "('delievery','pkg" + str(i) + "',('city" + str(x1) + "','loc" + str(y1) + "')),"
		pyhop  = pyhop + "]," +order_str + ", 9)\n"
		declare_types = declare_types + "]})\n"
		loc_py = loc_py + "}\n"
		load_py = load_py + "}\n"

		f.writelines("#!/usr/bin/env python\n# coding=utf-8\nimport sys  \nsys.path.insert(0, './') \nfrom logistic import *\nimport new_tihtn_planner\n")
		f.writelines('state0 = new_tihtn_planner.State(\'state0\')\n\n')
		f.writelines("allow = False\n")
		f.writelines(loc_py)
		f.writelines(load_py)
		f.writelines(plane_num_py)
		f.writelines(declare_types)
		f.writelines(declare_funs)
		f.writelines(instance)
		f.writelines(pyhop)
		f.writelines("def add_methods(fun_obj_list):\n\tfor fun in fun_obj_list:\n\t\tnew_tihtn_planner.add_method(fun.func_name.split('__')[0], fun)\ndef reverse_methods():\n\tnew_tihtn_planner.reverse_methods()")
		f.close()


# generate_training_and_validating("./training/", "./validating/", 1, 75, 5, 1, 4, 1)
# generate_testing("./testing/", 1, 25, 5, 1, 4, 1)






    


