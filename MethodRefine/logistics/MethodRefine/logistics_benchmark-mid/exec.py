import sys
import os
import time
import copy
import generateBenchmark_logistic

training_path = "./training/" 
testing_path = "./testing/"
validating_path = "./validating/"
sys.path.insert(0, validating_path)
sys.path.insert(0, training_path)
sys.path.insert(0, testing_path)

def reduce_methods(all_methods, i):
    original = len(all_methods)
    new_all_methods = []
    for method in all_methods:
        print (method)
        if (method not in new_all_methods):
            new_all_methods.append(method)
    print ("Length of the Duplicate-removed methods completion is " + str(len(new_all_methods)))

    remove_duplicate = len(new_all_methods)
    index = 0
    import new_tihtn_planner
    new_methods_list = new_tihtn_planner.generate_methods("logistics", new_all_methods)
    while (index < len(new_methods_list)):
        new_methods_list_copy = copy.deepcopy(new_methods_list)
        delete = new_methods_list_copy[index]
        del new_methods_list_copy[index]
        import logistics_method_completion
        time.sleep(1)
        fun_obj_list = []
        for new_method_name in new_methods_list_copy:
            fun_obj = getattr(sys.modules["logistics_method_completion"], new_method_name)
            fun_obj_list.append(fun_obj)
        air_ship = getattr(sys.modules["logistic"], "air_ship")
        city_ship = getattr(sys.modules["logistic"], "city_ship")
        delievery = getattr(sys.modules["logistic"], "delievery")
        removable = True
        for vi in range(1, i + 1):
            exec("import " + "validating_" + str(vi))
            new_tihtn_planner.declare_methods('air_ship',air_ship)
            new_tihtn_planner.declare_methods('city_ship',city_ship)
            new_tihtn_planner.declare_methods('delievery', delievery)
            exec("validating_" + str(vi) + ".add_methods(fun_obj_list)")
            exec("validating_" + str(vi) + ".reverse_methods()")
            solution, orig = eval("validating_" + str(vi) + ".execute(False)")
            del sys.modules["validating_" + str(vi)]
            if (solution == []):
                removable = False
                break
        if (removable):
            print ("A method is removed:")
            print (delete)
            new_methods_list = new_methods_list_copy
        else:
            index += 1

    after_reduce = len(new_methods_list)
    print ("Length of the reduced method completion is " + str(after_reduce))
    return original, remove_duplicate, new_methods_list

def testing(reduced_methods,i):
    ft = open("result_of_" + str(i) + "training", "w")
    import new_tihtn_planner
    fun_obj_list = []
    for new_method_name in reduced_methods:
        fun_obj = getattr(sys.modules["logistics_method_completion"], new_method_name)
        fun_obj_list.append(fun_obj)
    air_ship = getattr(sys.modules["logistic"], "air_ship")
    city_ship = getattr(sys.modules["logistic"], "city_ship")
    delievery = getattr(sys.modules["logistic"], "delievery")

    testing_instances = os.listdir(testing_path)
    testing_instances.sort()
    total_testing = 0
    solved_instance = 0
    unsolved_instance = 0
    for instance in testing_instances:
        if (instance.find("pyc") != -1):
            continue
        exec("import " + instance.split(".")[0])
        new_tihtn_planner.declare_methods('air_ship',air_ship)
        new_tihtn_planner.declare_methods('city_ship',city_ship)
        new_tihtn_planner.declare_methods('delievery', delievery)
        exec(instance.split(".")[0] + ".add_methods(fun_obj_list)")
        exec(instance.split(".")[0] + ".reverse_methods()")
        begin = time.clock()
        solution, orig = eval(instance.split(".")[0] + ".execute(False)")
        end = time.clock()
        total_time = end - begin
        total_testing += 1
        if (solution == []):
            print ("failed to solve: " + instance)
            ft.write(instance + "\t" + str(total_time) + "\t" + "failed\n")
            unsolved_instance += 1
        else:
            print ("successfully solved: " + instance + "   " + str(total_time) + "s")
            ft.write(instance + "\t" + str(total_time) + "\t" + "successful\n")
            solved_instance += 1
        del sys.modules[instance.split(".")[0]]
    ft.close()
    del sys.modules["logistics_method_completion"]
    print ("number of total instance = " + str(total_testing))
    print ("number of solved instance = " + str(solved_instance))
    print ("number of unsolved instance = " + str(unsolved_instance))
    return solved_instance

# import logistic

fw = open("result", "w")
# make sure that there are 75 training instances and 75 validating instances and 25 testing instances 
all_methods = []
import new_tihtn_planner
import logistic
for i in range(1,76):
    print ("#################################################################################")
    print ("Doing the " + str(i) + " iteration")
    f = open("result_of_" + str(i) + "_training", "w")
    air_ship = getattr(sys.modules["logistic"], "air_ship")
    city_ship = getattr(sys.modules["logistic"], "city_ship")
    delievery = getattr(sys.modules["logistic"], "delievery")
    new_tihtn_planner.declare_methods('air_ship',air_ship)
    new_tihtn_planner.declare_methods('city_ship',city_ship)
    new_tihtn_planner.declare_methods('delievery', delievery)
    import_str = "import " + "training_" + str(i)
    exec(import_str)
    # print ("solving " + instance)
    pyhop_str = "training_" + str(i) + ".execute(True)"
    begin = time.clock()
    solution, generalized_methods = eval(pyhop_str)
    end = time.clock()
    total_time = end - begin
    print ("training_" + str(i) + ".py" + " is solved in " + str(total_time) + "s")
    fw.write("training_" + str(i) + ".py" + "\t" + str(total_time) + "\n")
    fw.flush()
    all_methods = all_methods + generalized_methods
    orig, de_dup, reduced_methods = reduce_methods(all_methods, i)
    fw.write(str(orig) + " methods from the frist " + str(i) + " tree(s)\n")
    fw.write(str(de_dup) + " methods left after removing the duplicate\n")
    fw.write(str(len(reduced_methods)) + " methods left after reducing\n")
    fw.flush()
    print ("Reducing is done")
    solved = testing(reduced_methods, i)
    fw.write(str(solved) + " testing instances are solved\n")
    print ("Testing is done")
fw.close()





