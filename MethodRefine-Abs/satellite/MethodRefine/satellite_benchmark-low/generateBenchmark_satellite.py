# generateBenchmark.py
# coding=utf-8
# author=zhoujl
#！/usr/bin/python 
import time
import datetime
import random
import os

def generate_inst(num, list):
	ret = []
	for i in range(0, num):
		inst_num = list[i]
		for j in range(0, inst_num):
			inst = "inst" + "-" + str(i + 1) + "-" + str(j + 1)
			ret.append(inst)
	return ret

def generate_on_board(list):
	ret = {}
	for i in range(0, len(list)):
		sate_num = list[i].split("-")[1]
  		inst_num = list[i].split("-")[2]
  		ret.update({list[i]:"sate-" + str(sate_num)})
  		if (ret.has_key('sate-' + str(sate_num))):
  			ret['sate-' + str(sate_num)].append(list[i])
  		else:
  			ret.update({'sate-' + str(sate_num):[list[i]]})
  	return ret
#创建文件

def generate_training_and_validating(training_path, validating_path, number_bottom, number_up, sate, inst_bottom, inst_up, direc, mode, img):

	direc_num = direc
	mode_num = mode
	img_num = img
	sate_num = sate
	for index in range(number_bottom, number_up + 1):
		mode_dict = {}
		direc_dict = {}
		calib_target_dict = {}
		pointing_dict = {}

		inst_num_list = []
		for i in range(0, sate_num + 1):
			inst_num = random.randint(inst_bottom, inst_up)
			inst_num_list.append(inst_num)
		inst_list = generate_inst(sate_num, inst_num_list)

		on_board_dict = generate_on_board(inst_list)

		sate_num_str = 'state0.sate_num = ' + str(sate_num) + "\n"
		inst_num_str = 'state0.inst_num = ' + str(len(inst_list)) + "\n"
		mode_num_str = 'state0.mode_num = ' + str(mode_num) + "\n"
		direc_num_str = 'state0.direc_num = ' + str(direc_num) + "\n"
		img_num_str = 'state0.img_num = ' + str(img_num) + "\n"


		on_board_str = 'state0.on_board = {'
		mode_str = 'state0.mode = {'
		calib_target_str = 'state0.calib_target = {'
		calibrate_str = 'state0.calibrate = {'
		pointing_str = 'state0.pointing = {'
		power_avail_str = 'state0.power_avail = {'
		power_on_str = 'state0.power_on = {'
		have_img_str = 'state0.have_img = {'

		order_str = "["
		for i in range(0, img_num - 1):
			order = [i, i + 1]
			order_str = order_str + str(order) + ","
		order_str = order_str + "]"

		sample = random.sample(inst_list, mode_num)
		for i in range(0, mode_num):
			mode_dict.update({'mode-' + str(i + 1):[sample[i]]})
			mode_dict.update({sample[i]:'mode-' + str(i + 1)})
		for inst in inst_list:
			if (inst not in sample):
				i = random.randint(0, mode - 1)
				mode_dict.update({inst: 'mode-' + str(i + 1)})
				mode_dict['mode-' + str(i + 1)].append(inst)
		sample = random.sample(inst_list, direc_num)
		for i in range(0, direc_num):
			calib_target_dict.update({sample[i]:'direc-' + str(i + 1)})
		for inst in inst_list:
			if inst not in sample:
				i = random.randint(0, direc_num - 1)
				calib_target_dict.update({inst:'direc-' + str(i + 1)})
		for i in range(0, sate_num):
			rand_direc = random.randint(0, direc_num - 1)
			pointing_dict.update({'sate-' + str(i + 1):'direc-' + str(rand_direc + 1)})




		ft = open(training_path + "training_" + str(index) + ".py", "w")
		fv = open(validating_path + "validating_" + str(index) + ".py", "w")
		#写进py文件的每一行 

		declare_types = 'new_tihtn_planner.declare_types({'
		declare_funs = "new_tihtn_planner.declare_funs({switch_off:['satellite'],switch_on:['instrument', 'satellite'],turn_to:['satellite', 'direction'],calibrate:['instrument', 'satellite', 'direction'], take_img:['satellite', 'direction', 'instrument', 'mode']})\n"
		instance = 'new_tihtn_planner.instance()\n'
		pyhop = "def execute(completable):\n\treturn new_tihtn_planner.pyhop(completable, allow, state0,["

		declare_types = declare_types + "'satellite':["
		for i in range(0, sate_num):
			declare_types = declare_types + "'" + 'sate-' + str(i + 1) + "',"
		declare_types = declare_types + "],"

		declare_types = declare_types + "'instrument':["
		for i in range(0, len(inst_list)):
			declare_types = declare_types + "'" + inst_list[i] + "',"
		declare_types = declare_types + "],"

		declare_types = declare_types + "'mode':["
		for i in range(0, mode_num):
			declare_types = declare_types + "'" + 'mode-' + str(i + 1) + "',"
		declare_types = declare_types + "],"

		declare_types = declare_types + "'direction':["
		for i in range(0, direc_num):
			declare_types = declare_types + "'" + 'direc-' + str(i + 1) + "',"
		declare_types = declare_types + "]"

		declare_types = declare_types + "})\n"

		for a, b in on_board_dict.items():
			if (type(b) == list):
				on_board_str = on_board_str + "'" + a + "':" + str(b) + ","
			else:
				on_board_str = on_board_str + "'" + a + "':'" + b + "',"
		on_board_str = on_board_str + "}\n"

		for a,b in mode_dict.items():
			if (type(b) == list):
				mode_str = mode_str + "'" + a + "':" + str(b) + ","
			else:
				mode_str = mode_str + "'" + a + "':'" + b + "',"
		mode_str = mode_str + "}\n"

		for a,b in calib_target_dict.items():
			calib_target_str = calib_target_str + "'" + a + "':'" + b + "',"
		calib_target_str = calib_target_str + "}\n"

		for a,b in pointing_dict.items():
			pointing_str = pointing_str + "'" + a + "':'" + b + "',"
		pointing_str = pointing_str + "}\n"

		for i in range(0, sate_num):
			power_avail_str = power_avail_str + "'" + 'sate-' + str(i + 1) + "':" + 'True' + ","
		power_avail_str = power_avail_str + "}\n"

		for inst in inst_list:
			power_on_str = power_on_str + "'" + inst + "'" + ":False" + ","
		power_on_str = power_on_str + "}\n"

		for inst in inst_list:
			calibrate_str = calibrate_str + "'" + inst + "'" + ":False" + ","
		calibrate_str = calibrate_str + "}\n"

		for i in range(0, direc_num):
			have_img_str = have_img_str + "'direc-" + str(i + 1) + "':{"
			for j in range(0, mode_num):
				have_img_str = have_img_str + "'mode-" + str(j + 1) + "': False,"
			have_img_str = have_img_str + "},"
		have_img_str = have_img_str + "}\n"

		for i in range(0, img_num):
			rand_direc = random.randint(0, direc_num - 1)
			rand_mode = random.randint(0, mode_num - 1)
			pyhop = pyhop + "('get_img','direc-" + str(rand_direc + 1) + "', 'mode-" + str(rand_mode + 1) + "'),"
		pyhop = pyhop + "], " + order_str + ",9)\n"





		ft.writelines("#!/usr/bin/env python\n# coding=utf-8\nimport sys  \nsys.path.insert(0, './') \nfrom satellite import *\nimport new_tihtn_planner\n")
		ft.writelines('state0 = new_tihtn_planner.State(\'state0\')\n\n')
		ft.writelines("allow = True\n")
		ft.writelines(sate_num_str)
		ft.writelines(inst_num_str)
		ft.writelines(mode_num_str)
		ft.writelines(direc_num_str)
		ft.writelines(img_num_str)
		ft.writelines(on_board_str)
		ft.writelines(mode_str)
		ft.writelines(calib_target_str)
		ft.writelines(pointing_str)
		ft.writelines(power_avail_str)
		ft.writelines(power_on_str)
		ft.writelines(calibrate_str)
		ft.writelines(have_img_str)
		ft.writelines(declare_types)
		ft.writelines(declare_funs)
		ft.writelines(instance)
		ft.writelines(pyhop)
		ft.close()
		fv.writelines("#!/usr/bin/env python\n# coding=utf-8\nimport sys  \nsys.path.insert(0, './') \nfrom satellite import *\nimport new_tihtn_planner\n")
		fv.writelines('state0 = new_tihtn_planner.State(\'state0\')\n\n')
		fv.writelines("allow = False\n")
		fv.writelines(sate_num_str)
		fv.writelines(inst_num_str)
		fv.writelines(mode_num_str)
		fv.writelines(direc_num_str)
		fv.writelines(img_num_str)
		fv.writelines(on_board_str)
		fv.writelines(mode_str)
		fv.writelines(calib_target_str)
		fv.writelines(pointing_str)
		fv.writelines(power_avail_str)
		fv.writelines(power_on_str)
		fv.writelines(calibrate_str)
		fv.writelines(have_img_str)
		fv.writelines(declare_types)
		fv.writelines(declare_funs)
		fv.writelines(instance)
		fv.writelines(pyhop)
		fv.writelines("def add_methods(fun_obj_list):\n\tfor fun in fun_obj_list:\n\t\tnew_tihtn_planner.add_method(fun.func_name.split('__')[0], fun)\ndef reverse_methods():\n\tnew_tihtn_planner.reverse_methods()")
		fv.close()

def generate_testing(testing_path,number_bottom, number_up, sate, inst_bottom, inst_up, direc, mode, img):


	direc_num = direc
	mode_num = mode
	img_num = img
	sate_num = sate
	for index in range(number_bottom, number_up + 1):
		mode_dict = {}
		direc_dict = {}
		calib_target_dict = {}
		pointing_dict = {}

		inst_num_list = []
		for i in range(0, sate_num + 1):
			inst_num = random.randint(inst_bottom, inst_up)
			inst_num_list.append(inst_num)
		inst_list = generate_inst(sate_num, inst_num_list)

		on_board_dict = generate_on_board(inst_list)

		sate_num_str = 'state0.sate_num = ' + str(sate_num) + "\n"
		inst_num_str = 'state0.inst_num = ' + str(len(inst_list)) + "\n"
		mode_num_str = 'state0.mode_num = ' + str(mode_num) + "\n"
		direc_num_str = 'state0.direc_num = ' + str(direc_num) + "\n"
		img_num_str = 'state0.img_num = ' + str(img_num) + "\n"

		on_board_str = 'state0.on_board = {'
		mode_str = 'state0.mode = {'
		calib_target_str = 'state0.calib_target = {'
		calibrate_str = 'state0.calibrate = {'
		pointing_str = 'state0.pointing = {'
		power_avail_str = 'state0.power_avail = {'
		power_on_str = 'state0.power_on = {'
		have_img_str = 'state0.have_img = {'

		order_str = "["
		for i in range(0, img_num - 1):
			order = [i, i + 1]
			order_str = order_str + str(order) + ","
		order_str = order_str + "]"

		sample = random.sample(inst_list, mode_num)
		for i in range(0, mode_num):
			mode_dict.update({'mode-' + str(i + 1):[sample[i]]})
			mode_dict.update({sample[i]:'mode-' + str(i + 1)})
		for inst in inst_list:
			if (inst not in sample):
				i = random.randint(0, mode - 1)
				mode_dict.update({inst: 'mode-' + str(i + 1)})
				mode_dict['mode-' + str(i + 1)].append(inst)
		sample = random.sample(inst_list, direc_num)
		for i in range(0, direc_num):
			calib_target_dict.update({sample[i]:'direc-' + str(i + 1)})
		for inst in inst_list:
			if inst not in sample:
				i = random.randint(0, direc_num - 1)
				calib_target_dict.update({inst:'direc-' + str(i + 1)})
		for i in range(0, sate_num):
			rand_direc = random.randint(0, direc_num - 1)
			pointing_dict.update({'sate-' + str(i + 1):'direc-' + str(rand_direc + 1)})
		for i in range(0, direc_num):
			have_img_str = have_img_str + "'direc-" + str(i + 1) + "':{"
			for j in range(0, mode_num):
				have_img_str = have_img_str + "'mode-" + str(j + 1) + "': False,"
			have_img_str = have_img_str + "},"
		have_img_str = have_img_str + "}\n"




		f = open(testing_path + "testing_" + str(index) + ".py", "w")
		#写进py文件的每一行 

		declare_types = 'new_tihtn_planner.declare_types({'
		declare_funs = "new_tihtn_planner.declare_funs({switch_off:['satellite'],switch_on:['instrument', 'satellite'],turn_to:['satellite', 'direction'],calibrate:['instrument', 'satellite', 'direction'], take_img:['satellite', 'direction', 'instrument', 'mode']})\n"
		instance = 'new_tihtn_planner.instance()\n'
		pyhop = "def execute(completable):\n\treturn new_tihtn_planner.pyhop(completable, allow, state0,["

		declare_types = declare_types + "'satellite':["
		for i in range(0, sate_num):
			declare_types = declare_types + "'" + 'sate-' + str(i + 1) + "',"
		declare_types = declare_types + "],"

		declare_types = declare_types + "'instrument':["
		for i in range(0, len(inst_list)):
			declare_types = declare_types + "'" + inst_list[i] + "',"
		declare_types = declare_types + "],"

		declare_types = declare_types + "'mode':["
		for i in range(0, mode_num):
			declare_types = declare_types + "'" + 'mode-' + str(i + 1) + "',"
		declare_types = declare_types + "],"

		declare_types = declare_types + "'direction':["
		for i in range(0, direc_num):
			declare_types = declare_types + "'" + 'direc-' + str(i + 1) + "',"
		declare_types = declare_types + "]"

		declare_types = declare_types + "})\n"

		for a, b in on_board_dict.items():
			if (type(b) == list):
				on_board_str = on_board_str + "'" + a + "':" + str(b) + ","
			else:
				on_board_str = on_board_str + "'" + a + "':'" + b + "',"
		on_board_str = on_board_str + "}\n"

		for a,b in mode_dict.items():
			if (type(b) == list):
				mode_str = mode_str + "'" + a + "':" + str(b) + ","
			else:
				mode_str = mode_str + "'" + a + "':'" + b + "',"
		mode_str = mode_str + "}\n"

		for a,b in calib_target_dict.items():
			calib_target_str = calib_target_str + "'" + a + "':'" + b + "',"
		calib_target_str = calib_target_str + "}\n"

		for a,b in pointing_dict.items():
			pointing_str = pointing_str + "'" + a + "':'" + b + "',"
		pointing_str = pointing_str + "}\n"

		for i in range(0, sate_num):
			power_avail_str = power_avail_str + "'" + 'sate-' + str(i + 1) + "':" + 'True' + ","
		power_avail_str = power_avail_str + "}\n"

		for inst in inst_list:
			power_on_str = power_on_str + "'" + inst + "'" + ":False" + ","
		power_on_str = power_on_str + "}\n"

		for inst in inst_list:
			calibrate_str = calibrate_str + "'" + inst + "'" + ":False" + ","
		calibrate_str = calibrate_str + "}\n"

		for i in range(0, img_num):
			rand_direc = random.randint(0, direc_num - 1)
			rand_mode = random.randint(0, mode_num - 1)
			pyhop = pyhop + "('get_img','direc-" + str(rand_direc + 1) + "', 'mode-" + str(rand_mode + 1) + "'),"
		pyhop = pyhop + "], " + order_str + ",9)\n"

		f.writelines("#!/usr/bin/env python\n# coding=utf-8\nimport sys  \nsys.path.insert(0, './') \nfrom satellite import *\nimport new_tihtn_planner\n")
		f.writelines('state0 = new_tihtn_planner.State(\'state0\')\n\n')
		f.writelines("allow = False\n")
		f.writelines(sate_num_str)
		f.writelines(inst_num_str)
		f.writelines(mode_num_str)
		f.writelines(direc_num_str)
		f.writelines(img_num_str)
		f.writelines(on_board_str)
		f.writelines(mode_str)
		f.writelines(calib_target_str)
		f.writelines(pointing_str)
		f.writelines(power_avail_str)
		f.writelines(power_on_str)
		f.writelines(calibrate_str)
		f.writelines(have_img_str)
		f.writelines(declare_types)
		f.writelines(declare_funs)
		f.writelines(instance)
		f.writelines(pyhop)
		f.writelines("def add_methods(fun_obj_list):\n\tfor fun in fun_obj_list:\n\t\tnew_tihtn_planner.add_method(fun.func_name.split('__')[0], fun)\ndef reverse_methods():\n\tnew_tihtn_planner.reverse_methods()")
		f.close()

# number_bottom, number_up, sate, inst_bottom, inst_up, direc, mode, img
# generate_training_and_validating("./training/", "./validating/", 1, 75, 3, 2, 5, 5, 3, 4)
# generate_testing("./testing/", 1, 25, 3, 2, 5, 5, 3, 4)






    


