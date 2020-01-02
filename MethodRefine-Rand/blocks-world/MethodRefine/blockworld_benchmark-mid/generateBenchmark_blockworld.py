# generateBenchmark.py
# coding=utf-8
# author=zhoujl
#！/usr/bin/python 
import time
import datetime
import random
import os

def generate_init_list(block_num, pile_num):
	block = range(1, block_num + 1)
	rand_order = random.sample(block, block_num)
	init = []
	for i in range(0, pile_num):
		init.append([])
	for i in range(0, block_num):
		ran = random.randint(0,pile_num - 1)
		init[ran].append(rand_order[i])
	return init
#创建文件

def generate_training_and_validating(training_path, validating_path, number_bottom, number_up,block_num, pile_num):

	for index in range(number_bottom, number_up + 1):
		on_dict = {}
		down_dict = {}
		clear_dict = {}
		on_table_dict = {}

		for i in range(0, block_num):
			on_dict.update({'block-' + str(i + 1):'False'})

		for i in range(0, block_num):
			down_dict.update({'block-' + str(i + 1):'False'})

		for i in range(0, block_num):
			clear_dict.update({'block-' + str(i + 1):'False'})
		for i in range(0, block_num):
			on_table_dict.update({'block-' + str(i + 1):'False'})

		init_list = generate_init_list(block_num, pile_num)
		# update the initiation
		for pile in init_list:
			if (len(pile) == 0):
				continue
			else:
				on_table_dict.update({'block-' + str(pile[0]):'True'})
				clear_dict.update({'block-' + str(pile[-1]):'True'})
				if (len(pile) > 1):
					for i in range(0, len(pile) - 1):
						on_dict.update({'block-' + str(pile[i]) : 'block-' + str(pile[i + 1])})
						down_dict.update({'block-' + str(pile[i + 1]) : 'block-' + str(pile[i])})


		on_str = 'state0.on = {'
		down_str = 'state0.down = {'
		clear_str = 'state0.clear = {'
		on_table_str = 'state0.on_table = {'
		holding_str = 'state0.holding = False\n'



		for a, b in on_dict.items():
			if (b == 'False'):
				on_str = on_str + "'" + a + "':False,"
			else:
				on_str = on_str + "'" + a + "':'" + b + "',"
		on_str = on_str + "}\n"

		for a, b in down_dict.items():
			if (b == 'False'):
				down_str = down_str + "'" + a + "':False,"
			else:
				down_str = down_str + "'" + a + "':'" + b + "',"
		down_str = down_str + "}\n"

		for a, b in clear_dict.items():
			clear_str = clear_str + "'" + a + "':" + b + ","
		clear_str = clear_str + "}\n"

		for a, b in on_table_dict.items():
			on_table_str = on_table_str + "'" + a + "':" + b + ","
		on_table_str = on_table_str + "}\n"

		ft = open(training_path + "training_" + str(index) + ".py", "w")
		fv = open(validating_path + "validating_" + str(index) + ".py", "w")
		#写进py文件的每一行 

		declare_types = 'new_tihtn_planner.declare_types({'
		declare_funs = "new_tihtn_planner.declare_funs({pick_up:['block'],put_down:['block'],stack:['block', 'block'],checkpile1:['nothing'],checkpile2:['nothing'],checkpile3:['nothing'],checkpile4:['nothing']})\n"
		instance = 'new_tihtn_planner.instance()\n'
		pyhop = "def execute(completable):\n\treturn new_tihtn_planner.pyhop(completable, allow, state0,["

		declare_types = declare_types + "'block':["
		for i in range(0, block_num):
			declare_types = declare_types + "'" + 'block-' + str(i + 1) + "',"
		declare_types = declare_types + "],"

		declare_types = declare_types + "'nothing':[()]"

		declare_types = declare_types + "})\n"


		pyhop = pyhop + "('tower5','block-1','block-2', 'block-3', 'block-4', 'block-5')"
		pyhop = pyhop + "], " + "[]" + ",9)\n"





		ft.writelines("#!/usr/bin/env python\n# coding=utf-8\nimport sys  \nsys.path.insert(0, './') \nfrom blockworld import *\nimport new_tihtn_planner\n")
		ft.writelines('state0 = new_tihtn_planner.State(\'state0\')\n\n')
		ft.writelines("allow = True\n")
		ft.writelines(on_str)
		ft.writelines(down_str)
		ft.writelines(clear_str)
		ft.writelines(on_table_str)
		ft.writelines(holding_str)

		ft.writelines(declare_types)
		ft.writelines(declare_funs)
		ft.writelines(instance)
		ft.writelines(pyhop)
		ft.close()

		fv.writelines("#!/usr/bin/env python\n# coding=utf-8\nimport sys  \nsys.path.insert(0, './') \nfrom blockworld import *\nimport new_tihtn_planner\n")
		fv.writelines('state0 = new_tihtn_planner.State(\'state0\')\n\n')
		fv.writelines("allow = False\n")
		fv.writelines(on_str)
		fv.writelines(down_str)
		fv.writelines(clear_str)
		fv.writelines(on_table_str)
		fv.writelines(holding_str)

		fv.writelines(declare_types)
		fv.writelines(declare_funs)
		fv.writelines(instance)
		fv.writelines(pyhop)
		fv.writelines("def add_methods(fun_obj_list):\n\tfor fun in fun_obj_list:\n\t\tnew_tihtn_planner.add_method(fun.func_name.split('__')[0], fun)\ndef reverse_methods():\n\tnew_tihtn_planner.reverse_methods()")
		fv.close()

def generate_testing(testing_path,number_bottom, number_up, block_num, pile_num):


	for index in range(number_bottom, number_up + 1):
		on_dict = {}
		down_dict = {}
		clear_dict = {}
		on_table_dict = {}

		for i in range(0, block_num):
			on_dict.update({'block-' + str(i + 1):'False'})

		for i in range(0, block_num):
			down_dict.update({'block-' + str(i + 1):'False'})

		for i in range(0, block_num):
			clear_dict.update({'block-' + str(i + 1):'False'})
		for i in range(0, block_num):
			on_table_dict.update({'block-' + str(i + 1):'False'})

		init_list = generate_init_list(block_num, pile_num)
		# update the initiation
		for pile in init_list:
			if (len(pile) == 0):
				continue
			else:
				on_table_dict.update({'block-' + str(pile[0]):'True'})
				clear_dict.update({'block-' + str(pile[-1]):'True'})
				if (len(pile) > 1):
					for i in range(0, len(pile) - 1):
						on_dict.update({'block-' + str(pile[i]) : 'block-' + str(pile[i + 1])})
						down_dict.update({'block-' + str(pile[i + 1]) : 'block-' + str(pile[i])})


		on_str = 'state0.on = {'
		down_str = 'state0.down = {'
		clear_str = 'state0.clear = {'
		on_table_str = 'state0.on_table = {'
		holding_str = 'state0.holding = False\n'



		for a, b in on_dict.items():
			if (b == 'False'):
				on_str = on_str + "'" + a + "':False,"
			else:
				on_str = on_str + "'" + a + "':'" + b + "',"
		on_str = on_str + "}\n"

		for a, b in down_dict.items():
			if (b == 'False'):
				down_str = down_str + "'" + a + "':False,"
			else:
				down_str = down_str + "'" + a + "':'" + b + "',"
		down_str = down_str + "}\n"

		for a, b in clear_dict.items():
			clear_str = clear_str + "'" + a + "':" + b + ","
		clear_str = clear_str + "}\n"

		for a, b in on_table_dict.items():
			on_table_str = on_table_str + "'" + a + "':" + b + ","
		on_table_str = on_table_str + "}\n"

		f = open(testing_path + "testing_" + str(index) + ".py", "w")
		#写进py文件的每一行 

		declare_types = 'new_tihtn_planner.declare_types({'
		declare_funs = "new_tihtn_planner.declare_funs({pick_up:['block'],put_down:['block'],stack:['block', 'block'],checkpile1:['nothing'],checkpile2:['nothing'],checkpile3:['nothing'],checkpile4:['nothing']})\n"
		instance = 'new_tihtn_planner.instance()\n'
		pyhop = "def execute(completable):\n\treturn new_tihtn_planner.pyhop(completable, allow, state0,["

		declare_types = declare_types + "'block':["
		for i in range(0, block_num):
			declare_types = declare_types + "'" + 'block-' + str(i + 1) + "',"
		declare_types = declare_types + "],"

		declare_types = declare_types + "'nothing':[()]"

		declare_types = declare_types + "})\n"


		pyhop = pyhop + "('tower5','block-1','block-2', 'block-3', 'block-4', 'block-5')"
		pyhop = pyhop + "], " + "[]" + ",9)\n"

		
		f.writelines("#!/usr/bin/env python\n# coding=utf-8\nimport sys  \nsys.path.insert(0, './') \nfrom blockworld import *\nimport new_tihtn_planner\n")
		f.writelines('state0 = new_tihtn_planner.State(\'state0\')\n\n')
		f.writelines("allow = False\n")
		f.writelines(on_str)
		f.writelines(down_str)
		f.writelines(clear_str)
		f.writelines(on_table_str)
		f.writelines(holding_str)

		f.writelines(declare_types)
		f.writelines(declare_funs)
		f.writelines(instance)
		f.writelines(pyhop)
		f.writelines("def add_methods(fun_obj_list):\n\tfor fun in fun_obj_list:\n\t\tnew_tihtn_planner.add_method(fun.func_name.split('__')[0], fun)\ndef reverse_methods():\n\tnew_tihtn_planner.reverse_methods()")
		f.close()

# number_bottom, number_up, sate, inst_bottom, inst_up, direc, mode, img
# generate_training_and_validating("./training/", "./validating/", 1, 50, 5, 4)
# generate_testing("./testing/", 1, 50, 5, 4)






    


