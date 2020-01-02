import copy
import random
def auto_calibrate__1(state, instrument):

	return [('calibrate',instrument,state.on_board[instrument],state.calib_target[instrument]),('turn_to',state.on_board[instrument],"direc-1")], []
def activate__1(state, instrument, satellite, direction):

	return [('switch_off',satellite),('switch_on',instrument,satellite),('auto_calibrate',instrument),('turn_to',satellite,direction),('turn_to',satellite,direction)], [[0, 1], [1, 2], [3, 4]]
def get_img__1(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-1")], [[0, 1]]
def auto_calibrate__2(state, instrument):

	return [('calibrate',instrument,state.on_board[instrument],state.calib_target[instrument]),('turn_to',state.on_board[instrument],state.calib_target[instrument])], []
def get_img__2(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],direction)], [[0, 1]]
def get_img__3(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-5")], [[0, 1]]
def activate__2(state, instrument, satellite, direction):

	return [('switch_off',satellite),('switch_on',instrument,satellite),('auto_calibrate',instrument),('turn_to',satellite,direction)], [[0, 1], [1, 2]]
def activate__3(state, instrument, satellite, direction):

	return [('switch_off',satellite),('switch_on',instrument,satellite),('auto_calibrate',instrument),('turn_to',satellite,"direc-5"),('turn_to',satellite,"direc-4"),('turn_to',satellite,direction)], [[0, 1], [1, 2], [3, 4], [4, 5]]
def activate__4(state, instrument, satellite, direction):

	return [('switch_off',satellite),('switch_on',instrument,satellite),('auto_calibrate',instrument),('turn_to',satellite,"direc-2"),('turn_to',satellite,"direc-2")], [[0, 1], [1, 2], [3, 4]]
def auto_calibrate__3(state, instrument):

	return [('calibrate',instrument,state.on_board[instrument],state.calib_target[instrument]),('turn_to',state.on_board[instrument],"direc-5")], []
def get_img__4(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-5"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3]]
def activate__5(state, instrument, satellite, direction):

	return [('switch_off',satellite),('switch_on',instrument,satellite),('auto_calibrate',instrument),('turn_to',satellite,"direc-4")], [[0, 1], [1, 2]]
def auto_calibrate__4(state, instrument):

	return [('calibrate',instrument,state.on_board[instrument],state.calib_target[instrument]),('turn_to',state.on_board[instrument],"direc-2"),('turn_to',state.on_board[instrument],state.calib_target[instrument])], [[1, 2]]
def get_img__5(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-2")], [[0, 1]]
def auto_calibrate__5(state, instrument):

	return [('calibrate',instrument,state.on_board[instrument],state.calib_target[instrument]),('turn_to',state.on_board[instrument],state.calib_target[instrument]),('turn_to',state.on_board[instrument],"direc-2"),('turn_to',state.on_board[instrument],state.calib_target[instrument])], [[1, 2], [2, 3]]
def auto_calibrate__6(state, instrument):

	return [('calibrate',instrument,state.on_board[instrument],state.calib_target[instrument]),('turn_to',state.on_board[instrument],state.calib_target[instrument]),('turn_to',state.on_board[instrument],"direc-2")], [[1, 2]]
def activate__6(state, instrument, satellite, direction):

	return [('switch_off',satellite),('switch_on',instrument,satellite),('auto_calibrate',instrument),('turn_to',satellite,"direc-5"),('turn_to',satellite,direction)], [[0, 1], [1, 2], [3, 4]]
def get_img__6(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-2"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3]]
def get_img__7(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-4")], [[0, 1]]
def activate__7(state, instrument, satellite, direction):

	return [('switch_off',satellite),('switch_on',instrument,satellite),('auto_calibrate',instrument),('turn_to',satellite,"direc-1")], [[0, 1], [1, 2]]
def auto_calibrate__7(state, instrument):

	return [('calibrate',instrument,state.on_board[instrument],state.calib_target[instrument]),('turn_to',state.on_board[instrument],state.calib_target[instrument]),('turn_to',state.on_board[instrument],"direc-4")], [[1, 2]]
def auto_calibrate__8(state, instrument):

	return [('calibrate',instrument,state.on_board[instrument],state.calib_target[instrument]),('turn_to',state.on_board[instrument],"direc-2")], []
def activate__8(state, instrument, satellite, direction):

	return [('switch_off',satellite),('switch_on',instrument,satellite),('auto_calibrate',instrument),('turn_to',satellite,"direc-3")], [[0, 1], [1, 2]]
def auto_calibrate__9(state, instrument):

	return [('calibrate',instrument,state.on_board[instrument],state.calib_target[instrument]),('turn_to',state.on_board[instrument],state.calib_target[instrument]),('turn_to',state.on_board[instrument],state.calib_target[instrument])], [[1, 2]]
def activate__9(state, instrument, satellite, direction):

	return [('switch_off',satellite),('switch_on',instrument,satellite),('auto_calibrate',instrument),('turn_to',satellite,"direc-3"),('turn_to',satellite,"direc-2"),('turn_to',satellite,"direc-5"),('turn_to',satellite,direction)], [[0, 1], [1, 2], [3, 4], [4, 5], [5, 6]]
def activate__10(state, instrument, satellite, direction):

	return [('switch_off',satellite),('switch_on',instrument,satellite),('auto_calibrate',instrument),('turn_to',satellite,"direc-1"),('turn_to',satellite,"direc-2"),('turn_to',satellite,direction)], [[0, 1], [1, 2], [3, 4], [4, 5]]
def get_img__8(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-1"),('turn_to',state.on_board[instrument],"direc-1")], [[0, 1], [2, 3]]
def auto_calibrate__10(state, instrument):

	return [('calibrate',instrument,state.on_board[instrument],state.calib_target[instrument]),('turn_to',state.on_board[instrument],"direc-4")], []
def activate__11(state, instrument, satellite, direction):

	return [('switch_off',satellite),('switch_on',instrument,satellite),('auto_calibrate',instrument),('turn_to',satellite,"direc-5")], [[0, 1], [1, 2]]
def auto_calibrate__11(state, instrument):

	return [('calibrate',instrument,state.on_board[instrument],state.calib_target[instrument]),('turn_to',state.on_board[instrument],state.calib_target[instrument]),('turn_to',state.on_board[instrument],"direc-1")], [[1, 2]]
def get_img__9(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-3")], [[0, 1]]
def activate__12(state, instrument, satellite, direction):

	return [('switch_off',satellite),('switch_on',instrument,satellite),('auto_calibrate',instrument),('turn_to',satellite,"direc-4"),('turn_to',satellite,direction)], [[0, 1], [1, 2], [3, 4]]
def auto_calibrate__12(state, instrument):

	return [('calibrate',instrument,state.on_board[instrument],state.calib_target[instrument]),('turn_to',state.on_board[instrument],"direc-3")], []
def get_img__10(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-3"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3]]
def activate__13(state, instrument, satellite, direction):

	return [('switch_off',satellite),('switch_on',instrument,satellite),('auto_calibrate',instrument),('turn_to',satellite,"direc-4"),('turn_to',satellite,"direc-2")], [[0, 1], [1, 2], [3, 4]]
