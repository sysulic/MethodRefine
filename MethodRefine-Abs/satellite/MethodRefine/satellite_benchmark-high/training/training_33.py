#!/usr/bin/env python
# coding=utf-8
import sys  
sys.path.insert(0, './') 
from satellite import *
import new_tihtn_planner
state0 = new_tihtn_planner.State('state0')

allow = True
state0.sate_num = 3
state0.inst_num = 9
state0.mode_num = 3
state0.direc_num = 5
state0.img_num = 4
state0.on_board = {'inst-1-1':'sate-1','inst-2-4':'sate-2','inst-1-3':'sate-1','inst-1-2':'sate-1','sate-1':['inst-1-1', 'inst-1-2', 'inst-1-3'],'sate-2':['inst-2-1', 'inst-2-2', 'inst-2-3', 'inst-2-4'],'sate-3':['inst-3-1', 'inst-3-2'],'inst-3-2':'sate-3','inst-3-1':'sate-3','inst-2-2':'sate-2','inst-2-3':'sate-2','inst-2-1':'sate-2',}
state0.mode = {'inst-1-1':'mode-1','inst-2-4':'mode-1','inst-1-3':'mode-2','inst-1-2':'mode-2','mode-1':['inst-2-1', 'inst-1-1', 'inst-2-4'],'mode-2':['inst-3-2', 'inst-1-2', 'inst-1-3'],'mode-3':['inst-3-1', 'inst-2-2', 'inst-2-3'],'inst-3-2':'mode-2','inst-3-1':'mode-3','inst-2-2':'mode-3','inst-2-3':'mode-3','inst-2-1':'mode-1',}
state0.calib_target = {'inst-3-1':'direc-2','inst-1-1':'direc-3','inst-1-3':'direc-1','inst-1-2':'direc-5','inst-3-2':'direc-5','inst-2-4':'direc-4','inst-2-2':'direc-2','inst-2-3':'direc-2','inst-2-1':'direc-4',}
state0.pointing = {'sate-1':'direc-5','sate-2':'direc-3','sate-3':'direc-4',}
state0.power_avail = {'sate-1':True,'sate-2':True,'sate-3':True,}
state0.power_on = {'inst-1-1':False,'inst-1-2':False,'inst-1-3':False,'inst-2-1':False,'inst-2-2':False,'inst-2-3':False,'inst-2-4':False,'inst-3-1':False,'inst-3-2':False,}
state0.calibrate = {'inst-1-1':False,'inst-1-2':False,'inst-1-3':False,'inst-2-1':False,'inst-2-2':False,'inst-2-3':False,'inst-2-4':False,'inst-3-1':False,'inst-3-2':False,}
state0.have_img = {'direc-1':{'mode-1': False,'mode-2': False,'mode-3': False,},'direc-2':{'mode-1': False,'mode-2': False,'mode-3': False,},'direc-3':{'mode-1': False,'mode-2': False,'mode-3': False,},'direc-4':{'mode-1': False,'mode-2': False,'mode-3': False,},'direc-5':{'mode-1': False,'mode-2': False,'mode-3': False,},}
new_tihtn_planner.declare_types({'satellite':['sate-1','sate-2','sate-3',],'instrument':['inst-1-1','inst-1-2','inst-1-3','inst-2-1','inst-2-2','inst-2-3','inst-2-4','inst-3-1','inst-3-2',],'mode':['mode-1','mode-2','mode-3',],'direction':['direc-1','direc-2','direc-3','direc-4','direc-5',]})
new_tihtn_planner.declare_funs({switch_off:['satellite'],switch_on:['instrument', 'satellite'],turn_to:['satellite', 'direction'],calibrate:['instrument', 'satellite', 'direction'], take_img:['satellite', 'direction', 'instrument', 'mode']})
new_tihtn_planner.instance()
def execute(completable):
	return new_tihtn_planner.pyhop(completable, allow, state0,[('get_img','direc-5', 'mode-1'),('get_img','direc-5', 'mode-1'),('get_img','direc-1', 'mode-2'),('get_img','direc-3', 'mode-1'),], [[0, 1],[1, 2],[2, 3],],9)
