import os

logistic_training_path = "/home/cpl/AAAI2019/TIHTN/logistics_benchmark-low/training/"
logistic_testing_path = "/home/cpl/AAAI2019/TIHTN/logistics_benchmark-low/testing/"
target_path = "./raw_prob/"
i = 1
training_files = os.listdir(logistic_training_path)
training_files.sort()
for training_file in training_files:
    if (training_file.find(".pyc") != -1):
        continue
    location = {}
    tasks = []
    fr = open(logistic_training_path + training_file, "r")
    lines = fr.readlines()
    for line in lines:
        if (line.find("state0.loc") != -1):
            exec("location = {" + line.split("{")[1].split("}")[0] + "}")
        if (line.find("return new_tihtn_planner.pyhop(completable, allow, state0,[") != -1):
            exec("tasks = [" + line.split("allow, state0,[")[1].split("]")[0] + "]")
    fr.close()
    fw = open(target_path + str(i) + ".pddl", "w")



    fw.write("( define ( problem probname )\n\t( :domain logistics )\n\t( :requirements :strips :typing :equality )\n\t( :objects\n")
    fw.write("\t\ta1 - airplane\n")
    for j in range(1, 6):
        fw.write("\t\tc" + str(j) + " - city\n")
        fw.write("\t\tt" + str(j) + " - truck\n")
        fw.write("\t\tl" + str(j) + "1" + " - location\n")
        fw.write("\t\tl" + str(j) + "2" + " - location\n")
    for j in range(1, len(tasks) + 1):
        fw.write("\t\tp" + str(j) + " - obj\n")
    # for x in range(1, 6):
    #     for y in range(1, 3):
    #         for z in range(1, 6):
    #             for w in range(1, 3):
    #                 if (x != z or y != w):
    #                     fw.write("\t\t(different l" + str(x) + str(y) + " l" + str(z) + str(w) + ")\n")
    fw.write("\t)\n\n\t( :init\n")
    for j in range(1, 6):
        fw.write("\t\t(airport l" + str(j) + "1)\n")
        fw.write("\t\t(in-city l" + str(j) + "1 " + "c" + str(j) + ")\n")
        fw.write("\t\t(in-city l" + str(j) + "2 " + "c" + str(j) + ")\n")
    for j in range(1, 6):
        loc = location['truck' + str(j)]
        x = loc[0][-1]
        y = loc[1][-1]
        fw.write("\t\t(truck-at t" + str(j) + " l" + x + y + ")\n")
    loc = location['plane1']
    x = loc[0][-1]
    y = loc[1][-1]
    fw.write("\t\t(airplane-at a1 " + "l" + x + y + ")\n")
    for j in range(1, len(tasks) + 1):
        loc = location['pkg' + str(j)]
        x = loc[0][-1]
        y = loc[1][-1]
        fw.write("\t\t(obj-at p" + str(j) + " l" + x + y + ")\n")
    fw.write("\t)\n\n\t( :goal\n\t\t( and\n")
    for task in tasks:
        pkg = task[1][-1]
        x = task[2][0][-1]
        y = task[2][1][-1]
        fw.write("\t\t\t(obj-at p" + pkg + " l" + x + y + ")\n")
    fw.write("\t\t)\n")
    fw.write("\t)\n")
    fw.write(")")
    fw.close()
    i += 1

testing_files = os.listdir(logistic_testing_path)
testing_files.sort()
for testing_file in testing_files:
    if (testing_file.find(".pyc") != -1):
        continue
    location = {}
    tasks = []
    fr = open(logistic_testing_path + testing_file, "r")
    lines = fr.readlines()
    for line in lines:
        if (line.find("state0.loc") != -1):
            exec("location = {" + line.split("{")[1].split("}")[0] + "}")
        if (line.find("return new_tihtn_planner.pyhop(completable, allow, state0,[") != -1):
            exec("tasks = [" + line.split("allow, state0,[")[1].split("]")[0] + "]")
    fr.close()
    fw = open(target_path + str(i) + ".pddl", "w")



    fw.write("( define ( problem probname )\n\t( :domain logistics )\n\t( :requirements :strips :typing :equality )\n\t( :objects\n")
    fw.write("\t\ta1 - airplane\n")
    for j in range(1, 6):
        fw.write("\t\tc" + str(j) + " - city\n")
        fw.write("\t\tt" + str(j) + " - truck\n")
        fw.write("\t\tl" + str(j) + "1" + " - location\n")
        fw.write("\t\tl" + str(j) + "2" + " - location\n")
    for j in range(1, len(tasks) + 1):
        fw.write("\t\tp" + str(j) + " - obj\n")
    # for x in range(1, 6):
    #     for y in range(1, 3):
    #         for z in range(1, 6):
    #             for w in range(1, 3):
    #                 if (x != z or y != w):
    #                     fw.write("\t\t(different l" + str(x) + str(y) + " l" + str(z) + str(w) + ")\n")
    fw.write("\t)\n\n\t( :init\n")
    for j in range(1, 6):
        fw.write("\t\t(airport l" + str(j) + "1)\n")
        fw.write("\t\t(in-city l" + str(j) + "1 " + "c" + str(j) + ")\n")
        fw.write("\t\t(in-city l" + str(j) + "2 " + "c" + str(j) + ")\n")
    for j in range(1, 6):
        loc = location['truck' + str(j)]
        x = loc[0][-1]
        y = loc[1][-1]
        fw.write("\t\t(truck-at t" + str(j) + " l" + x + y + ")\n")
    loc = location['plane1']
    x = loc[0][-1]
    y = loc[1][-1]
    fw.write("\t\t(airplane-at a1 " + "l" + x + y + ")\n")
    for j in range(1, len(tasks) + 1):
        loc = location['pkg' + str(j)]
        x = loc[0][-1]
        y = loc[1][-1]
        fw.write("\t\t(obj-at p" + str(j) + " l" + x + y + ")\n")
    fw.write("\t)\n\n\t( :goal\n\t\t( and\n")
    for task in tasks:
        pkg = task[1][-1]
        x = task[2][0][-1]
        y = task[2][1][-1]
        fw.write("\t\t\t(obj-at p" + pkg + " l" + x + y + ")\n")
    fw.write("\t\t)\n")
    fw.write("\t)\n")
    fw.write(")")
    fw.close()
    i += 1