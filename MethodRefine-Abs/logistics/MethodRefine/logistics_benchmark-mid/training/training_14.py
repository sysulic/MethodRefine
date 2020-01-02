#!/usr/bin/env python
# coding=utf-8
import sys  
sys.path.insert(0, './') 
from logistic import *
import new_tihtn_planner
state0 = new_tihtn_planner.State('state0')

allow = True
state0.loc = {'truck1':('city1','loc1'),'truck2':('city2','loc1'),'truck3':('city3','loc1'),'truck4':('city4','loc2'),'truck5':('city5','loc1'),'plane1':('city1','loc1'),'pkg1':('city5','loc2'),'pkg2':('city3','loc2'),'pkg3':('city3','loc1'),}
state0.load = {'truck1':False,'truck2':False,'truck3':False,'truck4':False,'truck5':False,'plane1':False,}
state0.plane_nums = 1
new_tihtn_planner.declare_types({'location':[('city1','loc1'),('city1','loc2'),('city2','loc1'),('city2','loc2'),('city3','loc1'),('city3','loc2'),('city4','loc1'),('city4','loc2'),('city5','loc1'),('city5','loc2'),],'truck':['truck1','truck2','truck3','truck4','truck5',],'plane':['plane1',],'pkg':['pkg1','pkg2','pkg3',]})
new_tihtn_planner.declare_funs({load_plane:['pkg', 'location', 'plane'],load_truck:['pkg', 'location', 'truck'],by_plane:['plane', 'location'],drive_truck:['truck', 'location'], unload_truck:['pkg', 'location', 'truck'],unload_plane:['pkg', 'location', 'plane']})
new_tihtn_planner.instance()
def execute(completable):
	return new_tihtn_planner.pyhop(completable, allow, state0,[('delievery','pkg1',('city3','loc1')),('delievery','pkg2',('city4','loc2')),('delievery','pkg3',('city2','loc1')),],[[0, 1],[1, 2],], 9)
