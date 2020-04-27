#coding:utf-8
"""
The "travel from home to the park" example from my lectures.
Author: Dana Nau <nau@cs.umd.edu>, May 31, 2013
This file should work correctly in both Python 2.7 and Python 3.2.
"""

import new_tihtn_planner
import random
import copy

#state 表示状态 a表示agent  x,y表示变量

def load_plane(state,pkg,place,plane):
    if state.loc.has_key(pkg) and state.loc[pkg][0] == state.loc[plane][0] and state.loc[pkg][1] == state.loc[plane][1] and state.load[plane] == False and state.loc[pkg] == place:
        state.loc[pkg] = (plane, plane)
        state.load[plane] = pkg
        return state
    else: return False

def by_plane(state, plane, goal):
    if state.loc[plane][0] != goal[0]:
        tmp = (goal[0], state.loc[plane][1])
        state.loc[plane] = copy.deepcopy(tmp)
        return  state
    else: return False

def unload_plane(state, pkg, goal, plane):
    if state.loc.has_key(pkg) and state.loc[pkg][0] == plane and state.load[plane] == pkg and state.loc[plane] == goal:
        tmp = (goal[0], state.loc[plane][1])
        state.loc[pkg] = copy.deepcopy(tmp)
        state.load[plane] = False
        return state
    else: return False

    
def load_truck(state,pkg,place,truck):
    if state.loc.has_key(pkg) and state.loc[pkg][0] == state.loc[truck][0] and state.loc[pkg][1] == state.loc[truck][1] and state.load[truck] == False and state.loc[pkg] == place:
                    state.loc[pkg] = (truck, truck)
                    state.load[truck] = pkg
                    return state
    else: return False

def drive_truck(state,truck,goal):
    if state.loc[truck][1] != goal[1] and state.loc[truck][0] == goal[0]:
        tmp = (state.loc[truck][0], goal[1])
        state.loc[truck] = copy.deepcopy(tmp)
        return  state
    else: return False

def unload_truck(state, pkg, goal, truck):
    if state.loc.has_key(pkg) and state.loc[pkg][0] == truck and state.loc[pkg][1] == truck and state.load[truck] == pkg and state.loc[truck] == goal:
        tmp = (state.loc[truck][0], goal[1])
        state.loc[pkg] = copy.deepcopy(tmp)
        state.load[truck] = False
        return state
    else: return False

#可以看出，如何声明operator
new_tihtn_planner.declare_operators(load_plane, by_plane, unload_plane, load_truck, drive_truck, unload_truck)
print('')
new_tihtn_planner.print_operators()


#############################上面表示operator，下面表示method########################

#可以看出每一个method也是有条件的
def air_ship(state,pkg,goal):
    # i = random.randint(1, state.plane_nums)
    i = 1
    plane = 'plane' + str(i)
    return [('load_plane',pkg, (copy.deepcopy(state.loc[pkg][0]), 'loc1'), plane),('by_plane', plane, goal), ('unload_plane',pkg, goal, plane)], [[0,1],[1,2]]


def city_ship(state,pkg,goal):
    truck = 'truck' + goal[0][4:]
    return [('load_truck',pkg,(copy.deepcopy(goal[0]), 'loc' + str(3 - int(goal[1][-1]))),truck), ('drive_truck', truck, goal), ('unload_truck',pkg,goal,truck)], [[0,1],[1,2]]



def delievery(state, pkg, goal):
    if state.loc[pkg][0] != goal[0] and goal[1] != 'loc1' and state.loc[pkg][1] != 'loc1':
        return [('city_ship',pkg, (copy.deepcopy(state.loc[pkg][0]), 'loc1')), ('air_ship',pkg,(copy.deepcopy(goal[0]), 'loc1')), ('city_ship',pkg,(copy.deepcopy(goal[0]), 'loc2'))],[[0,1], [1,2]]
    if state.loc[pkg][0] == goal[0] and state.loc[pkg][1] != goal[1]:
        return [('city_ship',pkg, goal)],[]
    if state.loc[pkg][0] != goal[0] and goal[1] == 'loc1' and state.loc[pkg][1] != 'loc1':
        return [('city_ship',pkg, (copy.deepcopy(state.loc[pkg][0]), 'loc1')), ('air_ship',pkg,(copy.deepcopy(goal[0]), 'loc1'))],[[0,1]]
    if state.loc[pkg][1] == 'loc1' and goal[1] == 'loc2':
        return [('air_ship',pkg,(copy.deepcopy(goal[0]), 'loc1')), ('city_ship',pkg,(copy.deepcopy(goal[0]), copy.deepcopy(goal[1])))],[[0,1]]
    if goal[1] == 'loc1':
        return [('air_ship',pkg,(copy.deepcopy(goal[0]), 'loc1'))], []



new_tihtn_planner.declare_methods('air_ship',air_ship)
new_tihtn_planner.declare_methods('city_ship',city_ship)
new_tihtn_planner.declare_methods('delievery', delievery)

new_tihtn_planner.declare_priority({2:['delievery'], 1:['city_ship','air_ship']})


new_tihtn_planner.print_methods()
###################################################################################
#可见，pshop中的state的表示是通过，字典来表示的

