import copy
import random
def auto_calibrate__1(state, instrument):

	return [('turn_to',state.on_board[instrument],state.calib_target[instrument]),('calibrate',instrument,state.on_board[instrument],state.calib_target[instrument])], [[0, 1]]
def activate__1(state, instrument, satellite, direction):

	return [('switch_off',satellite),('switch_on',instrument,satellite),('auto_calibrate',instrument)], [[0, 1], [1, 2]]
def auto_calibrate__2(state, instrument):

	return [('calibrate',instrument,state.on_board[instrument],state.calib_target[instrument])], []
def activate__2(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('auto_calibrate',instrument)], [[0, 1]]
def get_img__1(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('turn_to',state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode)], [[0, 1], [1, 2]]
def get_img__2(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode)], [[0, 1]]
