import copy
import random
def activate__1(state, instrument, satellite, direction):

	return [('switch_off',satellite),('switch_on',instrument,satellite)], [[0, 1]]
def activate__2(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite)], []
def get_img__1(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('turn_to',state.on_board[instrument],"direc-4"),('calibrate',instrument,state.on_board[instrument],"direc-4"),('turn_to',state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode)], [[0, 1], [1, 2], [2, 3], [3, 4]]
def get_img__2(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('turn_to',state.on_board[instrument],"direc-5"),('calibrate',instrument,state.on_board[instrument],"direc-5"),('turn_to',state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode)], [[0, 1], [1, 2], [2, 3], [3, 4]]
def get_img__3(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('turn_to',state.on_board[instrument],direction),('calibrate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode)], [[0, 1], [1, 2], [2, 3]]
def get_img__4(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('calibrate',instrument,state.on_board[instrument],"direc-2"),('turn_to',state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode)], [[0, 1], [1, 2], [2, 3]]
def get_img__5(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('calibrate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode)], [[0, 1], [1, 2]]
def get_img__6(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('calibrate',instrument,state.on_board[instrument],"direc-5"),('turn_to',state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode)], [[0, 1], [1, 2], [2, 3]]
def get_img__7(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('turn_to',state.on_board[instrument],"direc-2"),('calibrate',instrument,state.on_board[instrument],"direc-2"),('turn_to',state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode)], [[0, 1], [1, 2], [2, 3], [3, 4]]
def get_img__8(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('turn_to',state.on_board[instrument],"direc-3"),('calibrate',instrument,state.on_board[instrument],"direc-3"),('turn_to',state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode)], [[0, 1], [1, 2], [2, 3], [3, 4]]
def get_img__9(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('calibrate',instrument,state.on_board[instrument],"direc-3"),('turn_to',state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode)], [[0, 1], [1, 2], [2, 3]]
def get_img__10(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('turn_to',state.on_board[instrument],"direc-1"),('calibrate',instrument,state.on_board[instrument],"direc-1"),('turn_to',state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode)], [[0, 1], [1, 2], [2, 3], [3, 4]]
def get_img__11(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('calibrate',instrument,state.on_board[instrument],"direc-4"),('turn_to',state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode)], [[0, 1], [1, 2], [2, 3]]
def get_img__12(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('calibrate',instrument,state.on_board[instrument],"direc-1"),('turn_to',state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode)], [[0, 1], [1, 2], [2, 3]]
