import copy
import random
def get_img__1(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],direction)], [[0, 1]]
def get_img__2(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-3"),('turn_to',state.on_board[instrument],"direc-3"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3], [3, 4]]
def get_img__3(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-1"),('turn_to',state.on_board[instrument],"direc-1"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3], [3, 4]]
def get_img__4(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-2"),('turn_to',state.on_board[instrument],"direc-2"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3], [3, 4]]
def get_img__5(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-5"),('turn_to',state.on_board[instrument],"direc-5"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3], [3, 4]]
def get_img__6(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-5"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3]]
def get_img__7(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-2"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3]]
def get_img__8(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-4"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3]]
def get_img__9(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-3"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3]]
def get_img__10(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-4"),('turn_to',state.on_board[instrument],"direc-4"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3], [3, 4]]
def get_img__11(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-1"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3]]
def get_img__12(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],direction),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3]]
def get_img__13(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],direction),('turn_to',state.on_board[instrument],direction),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3], [3, 4]]
