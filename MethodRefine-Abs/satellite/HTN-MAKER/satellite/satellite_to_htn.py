import os
import sys
import new_tihtn_planner

satellite_training_path = "/home/cpl/AAAI2020/htn/root_prefer/satellite/MethodLearn/satellite_benchmark-high/training/"
satellite_testing_path = "/home/cpl/AAAI2020/htn/root_prefer/satellite/MethodLearn/satellite_benchmark-high/testing/"
target_path = "./htn_prob/"
sys.path.insert(0, satellite_training_path)
sys.path.insert(0, satellite_testing_path)
i = 1
training_files = os.listdir(satellite_training_path)
training_files.sort()
for training_file in training_files:
    if (training_file.find(".pyc") != -1):
        continue
    location = {}
    tasks = []
    fr = open(satellite_training_path + training_file, "r")
    lines = fr.readlines()
    for line in lines:
        if (line.find("return new_tihtn_planner.pyhop(completable, allow, state0,[") != -1):
            exec("tasks = [" + line.split("allow, state0,[")[1].split("]")[0] + "]")
    fr.close()
    exec("from " + training_file.split(".")[0] + " import *")
    fw = open(target_path + str(i) + ".htn", "w")
    fw.write("( define ( htn-problem probname )\n\t( :domain satellite )\n\t( :requirements :strips :htn :typing :equality )\n\t( :objects\n")
    for sate in new_tihtn_planner.types['satellite']:
        fw.write("\t\tsate" + sate.split("-")[1] + " - satellite\n")
    for direc in new_tihtn_planner.types['direction']:
        fw.write("\t\tdirec" + direc.split("-")[1] + " - direction\n")
    for mode in new_tihtn_planner.types['mode']:
        fw.write("\t\tmode" + mode.split("-")[1] + " - mode\n")
    for inst in new_tihtn_planner.types['instrument']:
        fw.write("\t\tinst" + inst.split("-")[1] + inst.split("-")[2] + " - instrument\n")

    fw.write("\t)\n\t( :init\n")
    for sate, direc in state0.pointing.items():
        fw.write("\t\t( pointing sate" + sate.split("-")[1] + " direc" + direc.split("-")[1] + " )\n")
    for index in range(1, state0.sate_num + 1):
        fw.write("\t\t( power_avail sate" + str(index) + " )\n")
        inst_list = state0.on_board["sate-" + str(index)]
        for inst in inst_list:
            fw.write("\t\t( on_board inst" + inst.split("-")[1] + inst.split("-")[2] + " sate" + str(index) + " )\n")
    for inst in new_tihtn_planner.types['instrument']:
        mode = state0.mode[inst]
        calib_target = state0.calib_target[inst]
        fw.write("\t\t( supports inst" + inst.split("-")[1] + inst.split("-")[2] + " mode" + mode.split("-")[1] + " )\n")
        fw.write("\t\t( calibration_target inst" + inst.split("-")[1] + inst.split("-")[2] + " direc" + calib_target.split("-")[1] + " )\n")
        fw.write("\t\t( not_calibrated inst" + inst.split("-")[1] + inst.split("-")[2] + " )\n")
    fw.write("\t)\n\t( :tasks\n")
    for task in tasks:
        direc = task[1]
        mode = task[2]
        fw.write("\t\t\t( GET_IMAGE direc" + direc.split("-")[1] + " mode" + mode.split("-")[1] + " )\n")
    fw.write("\t)\n)")

    fw.close()
    i += 1

testing_files = os.listdir(satellite_testing_path)
testing_files.sort()
for testing_file in testing_files:
    if (testing_file.find(".pyc") != -1):
        continue
    location = {}
    tasks = []
    fr = open(satellite_testing_path + testing_file, "r")
    lines = fr.readlines()
    for line in lines:
        if (line.find("return new_tihtn_planner.pyhop(completable, allow, state0,[") != -1):
            exec("tasks = [" + line.split("allow, state0,[")[1].split("]")[0] + "]")
    fr.close()
    exec("from " + testing_file.split(".")[0] + " import *")
    fw = open(target_path + str(i) + ".htn", "w")
    fw.write("( define ( htn-problem probname )\n\t( :domain satellite )\n\t( :requirements :strips :htn :typing :equality )\n\t( :objects\n")
    for sate in new_tihtn_planner.types['satellite']:
        fw.write("\t\tsate" + sate.split("-")[1] + " - satellite\n")
    for direc in new_tihtn_planner.types['direction']:
        fw.write("\t\tdirec" + direc.split("-")[1] + " - direction\n")
    for mode in new_tihtn_planner.types['mode']:
        fw.write("\t\tmode" + mode.split("-")[1] + " - mode\n")
    for inst in new_tihtn_planner.types['instrument']:
        fw.write("\t\tinst" + inst.split("-")[1] + inst.split("-")[2] + " - instrument\n")

    fw.write("\t)\n\t( :init\n")
    for sate, direc in state0.pointing.items():
        fw.write("\t\t( pointing sate" + sate.split("-")[1] + " direc" + direc.split("-")[1] + " )\n")
    for index in range(1, state0.sate_num + 1):
        fw.write("\t\t( power_avail sate" + str(index) + " )\n")
        inst_list = state0.on_board["sate-" + str(index)]
        for inst in inst_list:
            fw.write("\t\t( on_board inst" + inst.split("-")[1] + inst.split("-")[2] + " sate" + str(index) + " )\n")
    for inst in new_tihtn_planner.types['instrument']:
        mode = state0.mode[inst]
        calib_target = state0.calib_target[inst]
        fw.write("\t\t( supports inst" + inst.split("-")[1] + inst.split("-")[2] + " mode" + mode.split("-")[1] + " )\n")
        fw.write("\t\t( calibration_target inst" + inst.split("-")[1] + inst.split("-")[2] + " direc" + calib_target.split("-")[1] + " )\n")
        fw.write("\t\t( not_calibrated inst" + inst.split("-")[1] + inst.split("-")[2] + " )\n")
    fw.write("\t)\n\t( :tasks\n")
    for task in tasks:
        direc = task[1]
        mode = task[2]
        fw.write("\t\t\t( GET_IMAGE direc" + direc.split("-")[1] + " mode" + mode.split("-")[1] + " )\n")
    fw.write("\t)\n)")

    fw.close()
    i += 1
