#coding:utf-8
from __future__ import print_function
import copy,sys, pprint
import Queue
import os

'''
Notes in implementations: 
1.here all implementations completely comply with pseudocode based on the python version of progression-based algorithm
'''

'''
Notes in all example(not this py file) to ensure all programs can be run:
1.function operator must return False, if characterized operator are not satisified the precondition
2.there must be "pyhop_tihtn.declare_operators" to declare all operators
3.there must be "pyhop_tihtn.declare_methods" to declare all method
4.there must be "pyhop_tihtn.declare_types" and "pyhop_tihtn.declare_funs" to specify
all parameters and operators of insertion
5.after Note 3, "pyhop_tihtn.instance()" must be called
6.at the same time, there must be basic instanition like "state1.hasWallet={'me':False}"
7.because of partial order,every method need add it."
'''
global allow_insertion
global tree_node_index
global num_of_plan
global num_of_inner_node
num_of_inner_node = 1
global plan_index


num_of_inner_node = 1

tree_structrue = []

symbol_table = []

insert_operators = []

stack = []

symbol_table_dict = {}

method_patch_dict = {}

types={}
funs={}
instances={}

methods_dict = {}

total_methods_count = {
    "tower1":1,
    "tower2":1,
    "tower3":1,
    "tower4":1,
    "tower5":1,
    "make_clear__1":1,
    "make_clear__2":1,
}

argm_dict = {
    'tower5':"(state, block1, block2, block3, block4, block5)",
    'tower4':"(state, block1, block2, block3, block4)",
    'tower3':"(state, block1, block2, block3)",
    'tower2':"(state, block1, block2)",
    'tower1':"(state, block1)",
    'make_clear__1':"(state, block)",
    'make_clear__2':"(state, block)"
}

func_argm_dict = {
    'pick_up':["block"],
    'put_down':["block"],
    'stack':["block_up", "block_down"],
    'checkpile1':["nothing"],
    'checkpile2':["nothing"],
    'checkpile3':["nothing"],
    'checkpile4':["nothing"],
    'tower5':["block1", "block2", "block3", "block4", "block5"],
    'tower4':["block1", "block2", "block3", "block4"],
    'tower3':["block1", "block2", "block3"],
    'tower2':["block1", "block2"],
    'tower1':["block1"],
    'make_clear__1':["block"],
    'make_clear__2':["block"]

}

# orig_return_subtask = {
#     'tower5':['tower4','make_clear','checkpile4','pick_up','stack'],
#     'tower4':['tower3','make_clear','checkpile3','pick_up','stack'],
#     'tower3':['tower2','make_clear','checkpile2','pick_up','stack'],
#     'tower2':['tower1','make_clear','checkpile1','pick_up','stack'],
#     'tower1':['make_clear','pick_up','stack'],


#     'get_img':["activate","take_img"],
#     'activate':["switch_off","switch_on","auto_calibrate"],
#     'auto_calibrate':["turn_to","calibrate"]
# }

orig_return_params = {
    "tower5":{
        "tower4":['block1', 'block2', 'block3', 'block4'],
        "make_clear":['block5'],
        "checkpile4":["()"],
        'pick_up':['block5'],
        'stack':['block5', 'block4']
    },
    "tower4":{
        "tower3":['block1', 'block2', 'block3'],
        "make_clear":['block4'],
        "checkpile3":["()"],
        'pick_up':['block4'],
        'stack':['block4', 'block3']
    },
    "tower3":{
        "tower2":['block1', 'block2'],
        "make_clear":['block3'],
        "checkpile2":["()"],
        'pick_up':['block3'],
        'stack':['block3', 'block2']
    },
    "tower2":{
        "tower1":['block1'],
        "make_clear":['block2'],
        "checkpile1":["()"],
        'stack':['block2', 'block1']
    },
    "tower1":{
        "make_clear":['block1'],
        'put_down':['block1']
    },
    "make_clear__1":{
        "make_clear":['block_on'],
        'pick_up':['block_on'],
        'put_down':['block_on']
    },
    "make_clear__2":{
        'pick_up':[''],
        'put_down':['']
    }

}

inner_code = {
    'tower5':"\n\t",
    'tower4':"\n\t",
    'tower3':"\n\t",
    'tower2':"\n\t",
    'tower1':"\n\t",
    'make_clear__1':"\n\tif (state.clear[block] == False):\n\t\tblock_on = state.on[block]\n\t\t",
    'make_clear__2':"\n\tif (state.clear[block] == True):\n\t\t"
}

rear_code = {
    'make_clear__1':"\n\telse:\n\t\treturn False,[]\n",
    'make_clear__2':"\n\telse:\n\t\treturn False,[]\n",
    'tower5':"\n",
    'tower4':"\n",
    'tower3':"\n",
    'tower2':"\n",
    'tower1':"\n"
}

priority = {}

def declare_priority(dict):
    priority = copy.deepcopy(dict)


def declare_types(_types):
    for item in _types.items():
        types[item[0]]=item[1]

    return types


def declare_funs(_funs):
    for item in _funs.items():
        funs[item[0]]=item[1]
    return funs

# def define_new_func(func_code, func_name):
#     exec(func_code)
#     fw = open(func_name + ".py", "w")
#     fw.writelines(func_code)
#     fw.close()

def initiate_methods_dict(name, method):
    methods_dict.update({name, method})

# def add_method(name, new_method, index):
#     old_method = methods_dict[name]
#     old_method[index].append(new_method)
#     methods_dict.update({name:old_method})

def convert_to_dict(table, dict):
    for item in table:
        dict.update({str(item[0]): item[1]})


import itertools
#instaniation of all combination of function and parameters, such as 
def instance():
    #给出所有的函数可能的参数形式  {travel_by_taxi:[(a,x,y),(a,x,y),...]}原函数形式 def travel_by_taxi(state,a,x,y):

    for key in funs.keys():
        value=funs[key]
        collabration=list()
        for item in value:
            collabration.append(types[item])
        product=itertools.product(*collabration)

        instances[key]=list(product)
    return instances

############################################################
# States and goals

class State():
    """A state is just a collection of variable bindings."""
    def __init__(self,name):
        self.__name__ = name

class Goal():
    """A goal is just a collection of variable bindings."""
    def __init__(self,name):
        self.__name__ = name


### print_state and print_goal are identical except for the name

def print_state(state,indent=4):
    """Print each variable in state, indented by indent spaces."""
    if state != False:
        for (name,val) in vars(state).items():
            if name != '__name__':
                for x in range(indent): sys.stdout.write(' ')
                sys.stdout.write(state.__name__ + '.' + name)
                print(' =', val)
    else: print('False')

def print_goal(goal,indent=4):
    """Print each variable in goal, indented by indent spaces."""
    if goal != False:
        for (name,val) in vars(goal).items():
            if name != '__name__':
                for x in range(indent): sys.stdout.write(' ')
                sys.stdout.write(goal.__name__ + '.' + name)
                print(' =', val)
    else: print('False')

############################################################
# Helper functions that may be useful in domain models

def forall(seq,cond):
    """True if cond(x) holds for all x in seq, otherwise False."""
    for x in seq:
        if not cond(x): return False
    return True

def find_if(cond,seq):
    """
    Return the first x in seq such that cond(x) holds, if there is one.
    Otherwise return None.
    """
    for x in seq:
        if cond(x): return x
    return None

############################################################
# Commands to tell Pyhop what the operators and methods are


operators = {}
methods = {}

def declare_operators(*op_list):
    """
    Call this after defining the operators, to tell Pyhop what they are.
    op_list must be a list of functions, not strings.
    """
    #添加 dict，key是operator的名字，value是operator方法
    operators.update({op.__name__:op for op in op_list})
    print(operators)
    return operators

#这里声明的是一个复杂任务有一系列可以用以解决的分解方法
def declare_methods(task_name,*method_list):
    """
    Call this once for each task, to tell Pyhop what the methods are.
    task_name must be a string.
    method_list must be a list of functions, not strings.
    """
    method_patch_dict.update({task_name: {}})
    methods.update({task_name:list(method_list)})
    return methods[task_name]

def add_method(task_name, method_func):
    method_list = methods[task_name]
    method_list.append(method_func)
    methods.update({task_name:method_list})
    return methods[task_name]

def reverse_methods():
    for key in methods.keys():
        methods[key].reverse()

# def add_methods(task_name, *new_method_list):
#     # after insertion, the function can update the decomposing methods,
#     cur_method = methods[task_name]
#     cur_method.append(list(new_method_list))
#     methods.update(task_name:cur_method)


############################################################
# Commands to find out what the operators and methods are

def print_operators(olist=operators):
    """Print out the names of the operators"""
    print('OPERATORS:', ', '.join(olist))

def print_methods(mlist=methods):
    """Print out a table of what the methods are for each task"""
    print('{:<14}{}'.format('TASK:','METHODS:'))
    for task in mlist:
        print('{:<14}'.format(task) + ', '.join([f.__name__ for f in mlist[task]]))

############################################################

# The actual planner

def reset_dict(dict, *new_value):
    keys = list(dict.keys())
    for i in range(0, len(keys)):
        dict.update({keys[i]:new_value[i]})

def reset():
    global allow_insertion
    global plan_index
    global num_of_inner_node
    global func_argm_dict
    global stack
    global method_patch_dict
    global methods_dict
    global symbol_table
    global symbol_table_dict
    global tree_structrue
    global insert_operators

    tree_structrue = []
    methods_dict = {}
    method_patch_dict = {}

    global symbol_table
    global symbol_table_dict
    stack = []
    symbol_table = []
    symbol_table_dict = {}
    insert_operators = []
    reset_dict(total_methods_count,1,1,1,1,1,1,1)
    plan_index = 1
    num_of_inner_node = 1

def pyhop(completable, allow, state,tasks, orders, verbose = 9):
    """
    Try to find a plan that accomplishes tasks in state.
    If successful, return the plan. Otherwise return False.
    """
    global allow_insertion
    global plan_index
    global num_of_inner_node
    global func_argm_dict
    global stack
    global method_patch_dict
    global methods_dict
    global symbol_table
    global symbol_table_dict
    reset()

    allow_insertion = allow
    solution, ordered_orig_plan = main(state,tasks, orders)
    if (not completable):
        return solution,[]
    if (solution != []):
        generalized_methods = complete(ordered_orig_plan, solution)
    else:
        generalized_methods = []
    
    if (generalized_methods == False):
        print("argment error!\n")
    # if verbose>0: print('** pyhop, verbose={}: **\n   state = {}\n   tasks = {}'.format(verbose, state.__name__, tasks))
    return solution,generalized_methods
    #开始调用核心方法，其中tasks是任务，0表示当前的深度
    #[]是为了递归使用的，是引用变量，可以表示对应的递归深度的当前解

def complete(orig_plan, inserted_plan):
    method_patch = get_patch(orig_plan, inserted_plan)
    return method_patch
    # triple:method name, original return value, new patch
    # for item in method_patch:
    #     # 生成新的分解函数
    #     key1 = item[0]
    #     key2 = item[1]
    #     value = item[2]
    #     orig_method = key2.split("-")
    #     op_list = []
    #     for atom in value:
    #         op_list.append(atom[0])
    #     if cmp(orig_method, op_list) == 0:
    #         continue

    #     # 更新method_patch_dict
    #     if method_patch_dict[key1].has_key(key2):
    #         if method_patch_dict[key1][key2].count(value) >= 1:
    #             continue
    #         else:
    #             method_patch_dict[key1][key2].append(value)
    #     else:
    #         method_patch_dict[key1].update({key2: [value]})

    #     # 生成新方法并导入
    #     generate_and_import_and_declare(item[0], item[2])

def get_patch(orig_plan, inserted_plan):
    method_patch = []
    son_to_father = {}
    father_to_son = {}
    tmp_dict = {}
    for edge in tree_structrue:
        if (edge[1][0] != "T"):
            son_to_father.update({int(edge[1]): edge[0]})
            tmp_dict.update({edge[0]: []})
            father_to_son.update({edge[0]: []})
    for i in range(1, plan_index):
        father_to_son[son_to_father[i]].append(i)
    index = 0
    for i in range(0, len(orig_plan)):
        while (orig_plan[i][0] != inserted_plan[index]):
            # tmp_list = copy.deepcopy(list(inserted_plan[index]))
            # tmp_list[0] = tmp_list[0].split(":")[1]
            tmp_dict[son_to_father[orig_plan[i][1] + 1]].append(inserted_plan[index])
            index += 1
        tmp_dict[son_to_father[orig_plan[i][1] + 1]].append(inserted_plan[index])
        index += 1
    
    for method, patch in tmp_dict.items():
        # get all son of method
        sons = []
        for edge in tree_structrue:
            if (edge[0] == method):
                sons.append(edge[1])
        
        # insert the compound task
        for i in range(0, len(sons)):
            if (sons[-(i + 1)][0] == 'T'):
                if (i == 0):
                    patch.insert(0,symbol_table_dict[sons[-(i + 1)]])
                else:
                    index = patch.index(symbol_table_dict[sons[-i]])
                    patch.insert(index + 1, symbol_table_dict[sons[-(i + 1)]])
        method_patch_item = []
        method_patch_item.append(symbol_table_dict[method])

        method_patch_item.append(patch)
        method_patch.append(method_patch_item)
    return generalize(method_patch)

# def generate_and_import_and_declare(method_name, subtask_list):
#     new_method_name = method_name + str(total_methods_count[method_name])
#     total_methods_count[method_name] += 1
#     define_head = "def " + new_method_name + argm_dict[method_name] + ":"
#     ret = generate_return_string(subtask_list)
#     fun_code = define_head + "\n" + inner_code[method_name] + "\n\t" + ret + "\n"
    
#     f = open(new_method_name + ".py","w")
#     f.write(fun_code)
#     f.close()
#     __import__(new_method_name)

#     fun_obj = getattr(sys.modules[new_method_name], new_method_name)
#     add_method(method_name, fun_obj)

def generate_return_string(subtask_list):
    subtask_list_str = "[" + generate_tuple_for_child(subtask_list[0])
    for i in range(1, len(subtask_list)):
        subtask_list_str = subtask_list_str + "," + generate_tuple_for_child(subtask_list[i])
    subtask_list_str = subtask_list_str + "]"
    order_list = generate_orders(len(subtask_list))
    ret = "return " + subtask_list_str + ", " + str(order_list)
    return ret

def generate_tuple_for_child(child):
    child_str = "('" + child[0] + "'"
    for i in range(1, len(child)):
        child_str = child_str + "," + child[i]
    child_str = child_str + ")"
    return child_str

def generate_orders(num_of_subtask):
    res = []
    for i in range(0, num_of_subtask - 1):
        res.append([i, i + 1])
    return res
# 泛化
def generalize(grounded_methods):
    grounded_methods = function_to_ctask(grounded_methods)
    genearlized_methods = []
    for grounded_method in grounded_methods:
        genearlized_method = copy.deepcopy(grounded_method)
        father = grounded_method[0]
        children = grounded_method[1]
        grounded_argm_dict = {}
        father_grounded_argm = list(father[1:])
        father_argm = func_argm_dict[father[0]]
        for i in range(0, len(father_argm)):
            grounded_argm_dict.update({father_grounded_argm[i]:father_argm[i]})

        # construct the generalized argment dictionary
        for child in children:
            if (child[0].find("insert") != -1):continue
            child_grounded_argm = list(child[1:])
            child_argm = orig_return_params[father[0]][child[0]]
            for i in range(0, len(child_argm)):
                if (grounded_argm_dict.has_key(child_grounded_argm[i]) and grounded_argm_dict[child_grounded_argm[i]] != child_argm[i]):
                    return False
                grounded_argm_dict.update({child_grounded_argm[i]:child_argm[i]})

        # generalized the father
        father_list = list(father)
        for k in range(1, len(father_list)):
            father_list[k] = grounded_argm_dict[father_list[k]]
        genearlized_method[0] = tuple(father_list)
        
        # generalized the children
        for i in range(0, len(children)):
            atom = copy.deepcopy(children[i])
            atom_argm = list(atom[1:])
            for j in range(0,len(atom_argm)):
                if (grounded_argm_dict.has_key(atom_argm[j])):
                    atom_argm[j] = grounded_argm_dict[atom_argm[j]]
                elif (type(atom_argm[j]) == str):
                    atom_argm[j] = "\"" + atom_argm[j] + "\""
                else:
                    atom_argm[j] = "\"" + str(atom_argm[j]) + "\""
            atom_argm.insert(0,children[i][0].split(":")[-1])
            children[i] = tuple(atom_argm)
        genearlized_method[1] = children
        genearlized_methods.append(genearlized_method)

    return genearlized_methods

def generate_methods(domain, all_methods):
    global total_methods_count
    reset_dict(total_methods_count, 1,1,1,1,1,1,1)
    new_methods = []
    f = open(domain + "_method_completion.py", "w")
    f.write("import copy\n")
    f.write("import random\n")
    for method in all_methods:
        father = method[0]
        children = method[1]
        new_method_name = father[0] + "__" + str(total_methods_count[father[0]])
        total_methods_count[father[0]] += 1
        new_methods.append(new_method_name)
        define_head = "def " + new_method_name + argm_dict[father[0]] + ":"
        ret = generate_return_string(children)
        fun_code = define_head + inner_code[father[0]] + ret + rear_code[father[0]] + "\n"
        f.write(fun_code)
        f.flush()
    f.close()
    return new_methods

def function_to_ctask(method_list):
    ret = []
    for method in method_list:
        ret_item = []
        ret_item.append(method[0])
        ret_item.append([])
        children = method[1]
        for child in children:
            child_list = list(child)
            child_list[0] = child_list[0].split("__")[0]
            child = tuple(child_list)
            ret_item[1].append(child)
        ret.append(ret_item)
    return ret

    # fun_obj = getattr(sys.modules[new_method_name], new_method_name)
    # add_method(method_name, fun_obj)

#####################################################################
def execute(state,all_tasks):

    terminate = False
    primitive=all_tasks
    all_plan=[]
    while not check(primitive):
        insert = True
        for sub in primitive:
            if len(sub) == 0:
                continue
            operator = operators[sub[0][0]]
            execute = operator(state, *sub[0][1:])
            if execute:
                all_plan.append(sub[0])
                del sub[0]
                insert = False
                # 开始下一轮的查找
                break

        # 表示需要插入
        if insert:
            ###用以判断是否找到了插入的operator，如果没有找到也要返回，表示哪一步不能进行插入，否则回发生死循环
            inserted = False
            # 保存当前状态
            cur_state = copy.deepcopy(state)
            # 测试每一个operator
            for item in instances.items():
                test_operator = item[0]
                params = item[1]
                # 对于现在的operator test_operator现在需要将所有的参数都要测试一下
                # 测试每一个参数
                param_break2 = False
                for param in params:
                    # 深拷贝是为了回溯的时候状态不发生变化
                    test_state = test_operator(copy.deepcopy(cur_state), *param)
                    if test_state == False:
                        continue

                    # 插入一个operator后，接着查看现在是否有uncontraint operator可以执行
                    # 测试插入test_operator后哪一个uncontraint operator
                    un_operator_break = False
                    for item in primitive:
                        if len(item) == 0:
                            continue
                        un_operator = operators[item[0][0]]
                        re_test_state = un_operator(copy.deepcopy(test_state), *item[0][1:])
                        # 表示可以插入新的任务
                        if re_test_state != False:
                            all_plan += [('inserted:', test_operator.__name__, param)]
                            all_plan.extend(item[0])
                            del item[0]
                            un_operator_break = True
                            inserted = True
                            break
                    if un_operator_break == True:
                        param_break2 = True
                        break
                if param_break2 == True:
                    break
            # 表示没有找到要插入的原子，此时要返回结果，否则死循环
            if inserted == False:
                return False
    return all_plan

def checkPri(tasks):
    for sub_task in tasks:
        if sub_task[0] in methods:
            return False
    return True

#用以检测是否所有的primitive全部执行完毕
def check(primitive):

    for item in primitive:
        if len(item)!=0:
            return False
    return True

#modify the output
def output(result):
    res=[]
    for i, item in enumerate(result):
        if not isinstance(item[0],tuple):
            cur=['inserted:'+item[0].__name__]
            cur.extend(item[1])
            res.append(tuple(cur))

            insert_item = [str(i + 1) + " : " + item[0].__name__]
            insert_item.extend(item[1:])
            insert_operators.append(tuple(insert_item))
        else:
            res.append(item[0])
    return res

def main(state,tasks, orders):
    global num_of_inner_node
    global symbol_table
#    all_tasks = [[task] for task in tasks]
    for i in range(0, len(tasks)):
        label = "T" + str(num_of_inner_node + len(tasks) - i - 1)
        
        stack_item = []
        stack_item.append([])
        stack_item.append(label)
        stack.append(stack_item)
        symbol_table_item = [label, tasks[-(i + 1)]]
        symbol_table.append(symbol_table_item)
    num_of_inner_node += len(tasks)
    for i in range(len(tasks)):
        tasks[i] = [tasks[i],i]
    result, plan_in_order = progression_planner([], [], state, tasks, orders)
    convert_to_dict(symbol_table, symbol_table_dict)
    #enrich information of output
    if result!=False:
        return output(result), plan_in_order
    else:
        return [],[]

def find_pre(all_tasks, orders):
    keys = set()
    all_indexs = set()
    for task in all_tasks:
        all_indexs.add(task[1])
    for order in orders:
        if (order[0] in all_indexs and order[1] in all_indexs):
            keys.add(order[1])
    prekeys = list()
    for all_task in all_tasks:
        if all_task[1] not in keys:
            prekeys.append(all_task[1])
    return prekeys

def update(orders, id):
    new_orders=list()
    for order in orders:
        if id != order[0]:
            new_orders.append(order)
    return new_orders
def find_precondition(orders, subTask_len):
    keys = set()
    for order in orders:
        keys.add(order[1])
    prekeys = list()
    for i in range(0, subTask_len):
        if i not in keys:
            prekeys.append(i)
    return prekeys

def find_sufcondition(orders, subTask_len):
    keys = set()
    for order in orders:
        keys.add(order[0])
    sufkeys = list()
    for i in range(0, subTask_len):
        if i not in keys:
            sufkeys.append(i)
    return sufkeys

def update_orders(j, subTask_len, sub_orders, orders):
    prekeys = find_precondition(sub_orders, subTask_len)
    sufkeys = find_sufcondition(sub_orders, subTask_len)
    for order in sub_orders:
        order[0] += j
        order[1] += j
    new_orders = list()
    for order in orders:
        if order[0] > j:
            order[0] += subTask_len - 1
        if order[1] > j:
            order[1] += subTask_len - 1
    tmp_order = []
    for order in orders:
        if (order[0] != order[1]):
            tmp_order.append(order)
    orders = tmp_order

    for order in orders:
        if order[0] == j:
            for sufkey in sufkeys:
                order[0] = sufkey+j
                new_orders.append(copy.deepcopy(order))
            if (subTask_len > 0):    
                continue
        if order[1] == j:
            for prekey in prekeys:
                order[1] = prekey+j
                new_orders.append(copy.deepcopy(order))
            if (subTask_len > 0):    
                continue
        new_orders.append(order)
    new_orders = new_orders + sub_orders
    return new_orders



#find the cyclic items
#if found, return next word that ought not to be choosed,otherwize, return False
#here is an important parameter: count to be set
#def findCyclic(plan):
#    last=len(plan)-1
#    count=0
#    for i in range(1,len(plan)):
#        while(last>=i and plan[last-i][0]==plan[last][0] and plan[last-i][1]==plan[last][1] ):
#            count+=1
#            last-=i
#            #count is the limit here 
#            if count>=2:
#                res=[]
#                for j in range(i):
#                    res.append(plan[last+j])
#                return res
#
#        last=len(plan)-1
#        count=0
#    return False
#

def count_operators(subtasks):
    count = 0
    for subtask in subtasks:
        if subtask[0][0] in operators:
            count += 1
    return count


def update_task_index(tasks, incremental):
    for i in range(len(tasks)):
        tasks[i][1] = i + incremental
    return tasks

def count_operators(subtasks):
    count = 0
    for subtask in subtasks:
        if subtask[0]in operators:
            count += 1
    return count

def progression_planner(orig_plan, cur_tasks, state, remain_tasks, orders):
    global num_of_inner_node
    global plan_index
    global tree_node_index
    global stack
    global tree_structrue
    global symbol_table

    if (len(remain_tasks) == 0):
        return cur_tasks, orig_plan
    if (remain_tasks[0][0][0] in operators):
        # for item in symbol_table:
        #     if (remain_tasks[0][0] == item[1]):
        #         index = item[0] - 1
        #         break
        index = len(orig_plan)
        op = operators[remain_tasks[0][0][0]]
        state_copy = copy.deepcopy(state)
        execute = op(state, *remain_tasks[0][0][1:])
        if execute:
            cur_tasks.append([remain_tasks[0][0], index])
            orig_plan.append([remain_tasks[0][0], index])
            del remain_tasks[0]
            result, original = progression_planner(orig_plan, cur_tasks, state, remain_tasks, orders)
            if (result == False):
                return False, False
            else:
                return result, original
        else:
            if (not allow_insertion):
                return False, False
            state = state_copy
            new_plan, original_plan, new_state = ff_complete(state, remain_tasks, orders, cur_tasks, orig_plan)
            # new_plan, original_plan, new_state = con_insert(state, remain_tasks, orders, cur_tasks, orig_plan)
            op = operators[remain_tasks[0][0][0]]
            execute = op(new_state, *remain_tasks[0][0][1:])
            original_plan.append([remain_tasks[0][0], index])
            new_plan.append([remain_tasks[0][0], index])
            del remain_tasks[0]
            result, original = progression_planner(original_plan, new_plan, execute, remain_tasks, orders)
            if (result == False):
                return False, False
            else:
                return result, original

    if (remain_tasks[0][0][0] in methods):
        relevant = methods[remain_tasks[0][0][0]]
        for method in relevant:
            subtasks,sub_orders = method(state, *remain_tasks[0][0][1:])
            if subtasks != False:
                num_of_ctask = len(subtasks) - count_operators(subtasks)
                for i in range(len(subtasks)):
                    subtasks[i] = [subtasks[i], -1]
                # global variable should be saved
                state_copy = copy.deepcopy(state)
                stack_copy = copy.deepcopy(stack)
                tree_structrue_copy = copy.deepcopy(tree_structrue)
                symbol_table_copy = copy.deepcopy(symbol_table)
                num_of_inner_node_copy = num_of_inner_node
                edge = stack.pop()
                new_father = edge[1]
                for item in symbol_table:
                    if item[0] == new_father:
                        tmp = list(item[1])
                        tmp[0] = method.func_name
                        item[1] = tuple(tmp)
                delta_num_of_inner_node = 0
                for i in range(0, len(subtasks)):
                    
                    if subtasks[len(subtasks) - 1 - i][0][0] in operators:
                        label = "L"
                    else:
                        label = "T" + str(num_of_inner_node + num_of_ctask - delta_num_of_inner_node - 1)
                        delta_num_of_inner_node += 1
                    tree_structrue_item = []
                    tree_structrue_item.append(new_father)
                    tree_structrue_item.append(label)
                    tree_structrue.append(tree_structrue_item)

                    symbol_table_item = []
                    symbol_table_item.append(label)
                    symbol_table_item.append(subtasks[len(subtasks) - 1 - i][0])
                    symbol_table.append(symbol_table_item)

                    # stack_item = []
                    # stack_item.append(new_father)
                    stack.append(tree_structrue_item)
                num_of_inner_node += delta_num_of_inner_node
                rear = 1
                while (len(stack) != 0 and stack[-1][1] == "L"):
                    if (tree_structrue[len(tree_structrue) - rear][1] != 'L'):
                        rear += 1
                        continue
                    tree_structrue[len(tree_structrue) - rear][1] = plan_index
                    symbol_table[len(symbol_table) - rear][0] = plan_index
                    end_edge = stack.pop()
                    end_edge[1] = str(plan_index)
                    plan_index += 1
                    rear += 1
                # _subtask_copy=copy.deepcopy(subtask_copy)
                # _subtask_copy.extend(subtasks)
                # new_task= _subtask_copy
                copy_orders = copy.deepcopy(orders)
                copy_remain_tasks=copy.deepcopy(remain_tasks)
                # copy_state=copy.deepcopy(state)
                del remain_tasks[0]
                remain_tasks = subtasks + remain_tasks
                new_orders = update_orders(len(orig_plan), len(subtasks), sub_orders, orders)
                remain_tasks = update_task_index(remain_tasks, len(orig_plan))
                result, plan_in_order = progression_planner(orig_plan, cur_tasks, state,remain_tasks, new_orders)
                #如果结果不符合，则回溯
                if result==False:
                    #回溯回来，考虑下一个分解的方法
                    state = state_copy
                    tree_structrue = tree_structrue_copy
                    stack = stack_copy
                    symbol_table = symbol_table_copy
                    remain_tasks=copy_remain_tasks
                    # state=copy_state
                    orders = copy_orders
                    plan_index -= rear - 1
                    num_of_inner_node = num_of_inner_node_copy
                    continue
                #否则返回结果
                else:
                    # global num_of_plan
                    # global num_of_inner_node
                    # global is_num_of_plan_changed
                    # if (not is_num_of_plan_changed):
                    #     num_of_plan = len(result)
                    #     is_num_of_plan_changed = True
                    # for i in range(0, len(subtasks)):
                    #     symbol_table_item = []
                    #     # append item from back to front
                    #     symbol_table_item.append(str(num_of_plan))
                    #     symbol_table_item.append(subtasks[len(subtasks) - 1 - i])
                    #     symbol_table.append(symbol_table_item)
                    #     num_of_plan -= 1
                    #     edge_in_tree = []
                    #     edge_in_tree.append("T" + str(num_of_inner_node) + " " + method.__name__)
                        
                    #     edge_in_tree.append(subtasks[len(subtasks) - 1 - i])
                    #     tree_structrue.append(edge_in_tree)
                    # symbol_table_item = []
                    # symbol_table_item.append("T" + str(num_of_inner_node))
                    # symbol_table_item.append(method.__name__)
                    # symbol_table.append(symbol_table_item)
                    # num_of_inner_node += 1
                    return result,plan_in_order
        return False,False
    return False, False



#get the (taskname,index)
def get_pre(all_tasks,orders):
    pres=find_pre(all_tasks,orders)
    results=[]
    for item in all_tasks:
        if item[1] in pres:
            results.append(item)
    return results


#if the function return results that means it successes, otherwise return False
def execute_update(state,all_tasks,orders,plan=[], ordered_orig_plan = []):#plan is used to store final result, inserted is used to store inserted operators
    #terminate for iteration by the orders
    
    if len(all_tasks)==0:
        return plan, ordered_orig_plan

    #call the unconstraint predecessor pres=query(all_tasks,orders)
    pres=get_pre(all_tasks,orders)
    #find the unconstraint operator
    uncons=[]
    for sub in pres:
            sub_op=sub[0]
            operator = operators[sub_op[0]]
            execute = operator(copy.deepcopy(state), *sub_op[1:])
            if execute:
                uncons.append(sub)
    if len(uncons)!=0:
        #because all the operators in uncons are able to be executed, there just pick out one to execute
        sub=uncons[0][0][0]
        sub_operator=operators[sub]
        execute = sub_operator(state, *uncons[0][0][1:])
        plan.append(uncons[0][0])
        ordered_orig_plan.append(uncons[0])
        #for test
        #print( output(plan))
        #here need update all_tasks and orders
        id=uncons[0][1]
        orders=update(orders,id)
        deleteTask(all_tasks,id)
        res_plan, orig_plan = execute_update(state,all_tasks,orders,plan, ordered_orig_plan)
        if res_plan != False:
            return res_plan, orig_plan
        return False, False
    elif (allow_insertion):
        inserted_plan, orig_plan, cur_state = con_insert(state,all_tasks,orders,plan, ordered_orig_plan)
        if inserted_plan == False:
            return False, False
        res_plan, orig_plan = execute_update(cur_state, all_tasks, orders, inserted_plan, ordered_orig_plan)
        return res_plan, orig_plan
    else:
        return False,False

#delete the completed tasks
def deleteTask(all_tasks,id):
    for i,item in enumerate(all_tasks):
        if id==item[1]:
            del all_tasks[i]
            break

#check whether the operator has been inserted.
def check_inserted(plan,operator):
    if len(plan)==0:
        return False
    index=len(plan)-1
    while not isinstance(plan[index][0],str) and index>=0:
        if operator!=plan[index]:
            index-=1
        else:
            return True
    return False
        
        

#possible related inserted operators
def related_insert(state,all_task,orders):
    pres=get_pre(all_task,orders)
    #find the unconstraint operator
    res=[]
    for sub in pres:
        sub_op=sub[0]
        operator = operators[sub_op[0]]
        res.append(set(funs[operator]))
    insertion=[]
    thredshold=1
    for item in instances.items():
        test_operator = item[0]
        types=set(funs[test_operator])
        _break=False
        for type in res:
            if len(type&types)>=thredshold:
                _break=True
                params = item[1]
                for param in params:
                    test_state = test_operator(copy.deepcopy(state), *param)
                    if test_state:
                        insertion.append((test_operator,param))
            if _break==True:
               break
    return insertion


def generate_instance_file(state, task):
    fw = open("insert.pddl", "w")
    fw.write(
        "(define (problem blocksworld-4-0)\n(:domain blocksworld)\n(:objects\n block-1 block-2 block-3 block-4 block-5 - block\n)\n")
    initial = {}
    initial.update({"block-1": (state.on_table["block-1"],state.clear["block-1"])})
    initial.update({"block-2": (state.on_table["block-2"],state.clear["block-2"])})
    initial.update({"block-3": (state.on_table["block-3"],state.clear["block-3"])})
    initial.update({"block-4": (state.on_table["block-4"],state.clear["block-4"])})
    initial.update({"block-5": (state.on_table["block-5"],state.clear["block-5"])})

    i = 1
    line = "(:init "
    for item in initial.keys():
        if (initial[item][0] == True):
            line = line + "(on-table " + item + ") "
    for item in initial.keys():
        if (initial[item][1] == True):
            line = line + "(clear " + item + ") "
    for item in state.on.keys():
        if (state.on[item] != False):
            line = line + "(on " + state.on[item] + " " + item + ") "
    if state.holding == False:
        line = line + "(hand-empty) "
    else:
        line = line + "(holding " + state.holding + ") "
    line = line + ")\n"
    fw.write(line)

    line = "(:goal (and "
    if (task[0] == "pick_up"):
        # line = line + "(on-table " + task[1] + ") "
        line = line + "(clear " + task[1] + ") "
        line = line + "(hand-empty) "
    elif (task[0] == "stack"):
        line = line + "(holding " + task[1] + ") "
        line = line + "(clear " + task[2] + ") "
    elif (task[0] == "put_down"):
        line = line + "(holding " + task[1] + ") "
    elif (task[0].find("checkpile") != -1):
        n = int(task[0][-1])
        line = line + "(on-table block-1 ) "
        for i in range(1, n):
            if (i is 1):
                continue
            line = line + "(on block-" + str(i) + "block-" + str(i - 1) + ") "
        line = line + "(clear block-" + str(n) + ") "
    fw.write(line + "))\n)")
    fw.close()


def ff_complete(state, all_tasks, orders, plan, ordered_orig_plan):
    pres = get_pre(all_tasks, orders)
    for task_and_order in pres:
        generate_instance_file(state, task_and_order[0])
        lines = os.popen("./ff -p ./ -o domain_htn.pddl -f insert.pddl").readlines()
        i = 0
        while (i < len(lines) and lines[i].find("step") == -1):
            i = i + 1
        if (i == len(lines)):
            continue
        while (lines[i].find(":") != -1):
            line = lines[i].split(":")[1].strip()
            completion = []
            params = []
            if (line.find("PICK-UP") != -1):
                func = getattr(sys.modules["blockworld"], "pick_up")
                completion.append(func)
                params.append(line.split(" ")[1].lower())
                tuple_params = tuple(params)
                completion.append(tuple_params)
                plan.append(completion)
                # state = func(state, line.split(" ")[1].lower())
            elif (line.find("PUT-DOWN") != -1):
                func = getattr(sys.modules["blockworld"], "put_down")
                completion.append(func)
                params.append(line.split(" ")[1].lower())
                completion.append(tuple(params))
                plan.append(completion)
                # state = func(state, line.split(" ")[1].lower())
            elif (line.find("STACK") != -1):
                func = getattr(sys.modules["blockworld"], "stack")
                completion.append(func)
                params.append(line.split(" ")[1].lower())
                params.append(line.split(" ")[2].lower())
                completion.append(tuple(params))
                plan.append(completion)
                # state = func(state, line.split(" ")[1].lower(), line.split(" ")[2].lower())
            elif (line.find("PICK-UP-FROM-BLOCK") != -1):
                func = getattr(sys.modules["blockworld"], "pick_up_from_block")
                completion.append(func)
                params.append(line.split(" ")[1].lower())
                params.append(line.split(" ")[2].lower())
                completion.append(tuple(params))
                plan.append(completion)
            state = func(state, *completion[1])
            i = i + 1
        return plan, ordered_orig_plan, state
    return False, False, False

#continue insert the operator
def con_insert(state,all_tasks,orders,plan, ordered_orig_plan):
        q = Queue.Queue()
        q.put((copy.deepcopy(state), copy.deepcopy(all_tasks), copy.deepcopy(orders), copy.deepcopy(plan)))
        while not q.empty():
            cur_state, cur_all_tasks, orders, cur_plan = q.get()
            
            # ket to speed up
            insertion=related_insert(cur_state, cur_all_tasks, orders)
            if(len(insertion) == 0):
                continue
            for select_op in insertion:
                sel_op=select_op[0]
                #store the current state
                cur_state_copy=copy.deepcopy(cur_state)
                sel_op(cur_state_copy,*select_op[1])
                if check_ocuur(cur_state_copy, cur_all_tasks, orders):
                    cur_plan.append(select_op)
                    return cur_plan, ordered_orig_plan, cur_state_copy
                else:
                    if check_inserted(cur_plan,select_op):
                        continue
                    copy_cur_plan = copy.deepcopy(cur_plan)
                    copy_cur_plan.append(select_op)
                    q.put((copy.deepcopy(cur_state_copy), copy.deepcopy(cur_all_tasks), copy.deepcopy(orders), copy.deepcopy(copy_cur_plan)))
        return False, False, False
       
    #    #find all operators satisfied with current state
    #     insertion=related_insert(state,all_tasks,orders)
    #     #terminate for iteration
    #     if len(insertion)==0:
    #         return False, False
    #     for select_op in insertion: 
    #         sel_op=select_op[0]
    #         #store the current state
    #         state_copy=copy.deepcopy(state)
    #         sel_op(state_copy,*select_op[1])
    #         #judge if there occurs the new unconstrained operator
    #         if check_ocuur(state_copy,all_tasks,orders):
    #             # 新形势下这个all_tasks已经可以执行
    #             copy_plan=copy.deepcopy(plan)
    #             copy_orders=copy.deepcopy(orders)
    #             copy_ordered_orig_plan = copy.deepcopy(ordered_orig_plan)
    #             #marked with the inserted operator
    #             plan.append(select_op)
    #             #for test
    #             #print( output(plan))
    #             #from this perspective, the excute_update must have return value.
    #             res_plan, orig_plan = execute_update(state_copy,all_tasks,orders,plan, ordered_orig_plan)
    #             if res_plan == False:
    #                plan=copy_plan
    #                orders=copy_orders
    #                ordered_orig_plan = copy_ordered_orig_plan
    #                continue
    #             else:
    #                return res_plan, orig_plan
    #         else:
    #             # 新形势下剩余的all_tasks仍然不可执行
    #             copy_plan=copy.deepcopy(plan)
    #             copy_orders=copy.deepcopy(orders)
    #             copy_ordered_orig_plan = copy.deepcopy(ordered_orig_plan)
    #             if check_inserted(plan,select_op):
    #                 continue
    #             plan.append(select_op)
    #             #for test
    #             #print( output(plan))
    #             #from this perspective, the con_insert must have return value.
    #             res_plan, orig_plan = con_insert(state_copy,all_tasks,orders,plan, ordered_orig_plan)
    #             if res_plan == False:
    #                 # print(output(plan))
    #                 plan=copy_plan
    #                 orders=copy_orders
    #                 ordered_orig_plan = copy_ordered_orig_plan
    #                 continue
    #             else:
    #                 #until backtrack stops,remove the last item of cylics(it has very strong programming skills here)
    #                 return res_plan, orig_plan
    #     #it means that need backtrack to find another primitive all_tasks
    #     return False,False

#check if there occurs unconstraint
# 检查在all_tasks中是否有前序任务可以在这个状态下执行
def check_ocuur(state,all_tasks,orders):
        pres=get_pre(all_tasks,orders)
        #find the unconstraint operator
        for sub in pres:
            operator = operators[sub[0][0]]
            execute = operator(copy.deepcopy(state), *sub[0][1:])
            if execute:
                return True
        return False



