import copy
import random
def get_img__1(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-4")], [[0, 1]]
def activate__1(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('calibrate',instrument,satellite,"direc-4"),('turn_to',satellite,direction)], [[1, 2]]
def get_img__2(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('calibrate',instrument,state.on_board[instrument],"direc-4")], [[0, 1]]
def get_img__3(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-3"),('switch_off',state.on_board[instrument]),('turn_to',state.on_board[instrument],"direc-4"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3], [3, 4], [4, 5]]
def get_img__4(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-4"),('calibrate',instrument,state.on_board[instrument],"direc-4"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3], [3, 4]]
def activate__2(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('switch_off',satellite),('calibrate',instrument,satellite,"direc-4")], [[1, 2]]
def activate__3(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('turn_to',satellite,"direc-5"),('switch_off',satellite),('calibrate',instrument,satellite,"direc-5"),('turn_to',satellite,direction)], [[1, 2], [2, 3], [3, 4]]
def get_img__5(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('calibrate',instrument,state.on_board[instrument],"direc-5")], [[0, 1]]
def get_img__6(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-1"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3]]
def activate__4(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('calibrate',instrument,satellite,"direc-1"),('turn_to',satellite,direction)], [[1, 2]]
def get_img__7(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('switch_off',state.on_board[instrument]),('turn_to',state.on_board[instrument],"direc-1"),('calibrate',instrument,state.on_board[instrument],"direc-1")], [[0, 1], [2, 3], [3, 4]]
def get_img__8(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-3"),('calibrate',instrument,state.on_board[instrument],"direc-3")], [[0, 1], [2, 3]]
def activate__5(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('turn_to',satellite,"direc-1"),('calibrate',instrument,satellite,"direc-3"),('calibrate',instrument,satellite,"direc-3")], [[1, 2], [2, 3]]
def get_img__9(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('switch_off',state.on_board[instrument]),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3]]
def get_img__10(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],direction)], [[0, 1]]
def get_img__11(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-2"),('turn_to',state.on_board[instrument],direction),('switch_off',"sate-1")], [[0, 1], [2, 3], [3, 4]]
def activate__6(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('calibrate',instrument,satellite,"direc-2")], []
def activate__7(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('calibrate',instrument,satellite,"direc-3"),('switch_off',satellite),('turn_to',satellite,direction)], [[1, 2], [2, 3]]
def activate__8(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('turn_to',satellite,direction)], []
def activate__9(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('calibrate',instrument,satellite,direction)], []
def get_img__12(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('calibrate',instrument,state.on_board[instrument],"direc-3"),('turn_to',state.on_board[instrument],"direc-1"),('switch_off',state.on_board[instrument]),('turn_to',state.on_board[instrument],"direc-3"),('calibrate',instrument,state.on_board[instrument],"direc-3")], [[0, 1], [2, 3], [3, 4], [4, 5], [5, 6]]
def activate__10(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('turn_to',satellite,"direc-3"),('calibrate',instrument,satellite,"direc-3"),('turn_to',satellite,direction)], [[1, 2], [2, 3]]
def get_img__13(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('switch_off',state.on_board[instrument]),('calibrate',instrument,state.on_board[instrument],"direc-3")], [[0, 1], [2, 3]]
def get_img__14(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-2"),('turn_to',state.on_board[instrument],"direc-5"),('turn_to',state.on_board[instrument],"direc-2"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3], [3, 4], [4, 5]]
def get_img__15(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('calibrate',instrument,state.on_board[instrument],"direc-2")], [[0, 1]]
def activate__11(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('calibrate',instrument,satellite,"direc-1"),('turn_to',satellite,"direc-1")], [[1, 2]]
def activate__12(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('switch_off',satellite),('calibrate',instrument,satellite,"direc-2")], [[1, 2]]
def get_img__16(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('switch_off',state.on_board[instrument]),('calibrate',instrument,state.on_board[instrument],"direc-1"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3], [3, 4]]
def get_img__17(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-4"),('calibrate',instrument,state.on_board[instrument],"direc-4"),('calibrate',instrument,state.on_board[instrument],"direc-4"),('turn_to',state.on_board[instrument],"direc-1"),('switch_off',state.on_board[instrument]),('turn_to',state.on_board[instrument],"direc-4"),('calibrate',instrument,state.on_board[instrument],"direc-4"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]
def get_img__18(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('switch_off',state.on_board[instrument])], [[0, 1]]
def activate__13(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('calibrate',instrument,satellite,"direc-4"),('turn_to',satellite,"direc-3"),('switch_off',satellite),('turn_to',satellite,"direc-4")], [[1, 2], [2, 3], [3, 4]]
def get_img__19(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-3"),('calibrate',instrument,state.on_board[instrument],"direc-3"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3], [3, 4]]
def activate__14(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('turn_to',satellite,"direc-1"),('calibrate',instrument,satellite,"direc-1"),('turn_to',satellite,direction)], [[1, 2], [2, 3]]
def activate__15(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('turn_to',satellite,"direc-3"),('turn_to',satellite,direction)], [[1, 2]]
def get_img__20(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('calibrate',instrument,state.on_board[instrument],"direc-3")], [[0, 1]]
def get_img__21(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-3"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3]]
def activate__16(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('calibrate',instrument,satellite,direction),('turn_to',satellite,"direc-1"),('turn_to',satellite,"direc-5"),('turn_to',satellite,direction),('calibrate',instrument,satellite,direction)], [[1, 2], [2, 3], [3, 4], [4, 5]]
def get_img__22(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('switch_off',state.on_board[instrument]),('turn_to',state.on_board[instrument],direction),('turn_to',state.on_board[instrument],direction),('calibrate',instrument,state.on_board[instrument],direction),('switch_off',state.on_board[instrument])], [[0, 1], [2, 3], [3, 4], [4, 5], [5, 6]]
def get_img__23(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('calibrate',instrument,state.on_board[instrument],"direc-3"),('switch_off',state.on_board[instrument])], [[0, 1], [2, 3]]
def get_img__24(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],direction),('calibrate',instrument,state.on_board[instrument],direction)], [[0, 1], [2, 3]]
def activate__17(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('calibrate',instrument,satellite,direction),('turn_to',satellite,"direc-1"),('switch_off',satellite),('turn_to',satellite,direction)], [[1, 2], [2, 3], [3, 4]]
def activate__18(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('turn_to',satellite,"direc-1")], []
def get_img__25(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('calibrate',instrument,state.on_board[instrument],"direc-1"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3]]
def get_img__26(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('calibrate',instrument,state.on_board[instrument],"direc-2"),('switch_off',state.on_board[instrument]),('turn_to',state.on_board[instrument],"direc-2")], [[0, 1], [2, 3], [3, 4]]
def activate__19(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('turn_to',satellite,"direc-1"),('calibrate',instrument,satellite,"direc-2"),('turn_to',satellite,direction)], [[1, 2], [2, 3]]
def activate__20(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('turn_to',satellite,"direc-5"),('calibrate',instrument,satellite,"direc-5"),('calibrate',instrument,satellite,"direc-5")], [[1, 2], [2, 3]]
def get_img__27(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('switch_off',state.on_board[instrument]),('turn_to',state.on_board[instrument],"direc-5"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3], [3, 4]]
def activate__21(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('turn_to',satellite,"direc-4"),('turn_to',satellite,direction)], [[1, 2]]
def activate__22(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('turn_to',satellite,"direc-5"),('switch_off',satellite),('calibrate',instrument,satellite,"direc-5"),('turn_to',satellite,"direc-5")], [[1, 2], [2, 3], [3, 4]]
def get_img__28(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('calibrate',instrument,state.on_board[instrument],"direc-5"),('turn_to',state.on_board[instrument],"direc-3"),('calibrate',instrument,state.on_board[instrument],"direc-5"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3], [3, 4], [4, 5]]
def activate__23(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('calibrate',instrument,satellite,"direc-5"),('turn_to',satellite,direction)], [[1, 2]]
def activate__24(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('turn_to',satellite,"direc-2"),('turn_to',satellite,direction)], [[1, 2]]
def get_img__29(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('switch_off',state.on_board[instrument]),('turn_to',state.on_board[instrument],"direc-5"),('switch_off',state.on_board[instrument]),('turn_to',state.on_board[instrument],"direc-4"),('calibrate',instrument,state.on_board[instrument],"direc-4"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
def activate__25(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('turn_to',satellite,"direc-4")], []
def get_img__30(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-2"),('calibrate',instrument,state.on_board[instrument],"direc-2"),('turn_to',state.on_board[instrument],"direc-4"),('switch_off',state.on_board[instrument]),('switch_off',state.on_board[instrument]),('turn_to',state.on_board[instrument],"direc-2"),('calibrate',instrument,state.on_board[instrument],"direc-2"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]
def activate__26(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('turn_to',satellite,"direc-2"),('calibrate',instrument,satellite,"direc-2")], [[1, 2]]
def activate__27(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('switch_off',satellite),('calibrate',instrument,satellite,"direc-5")], [[1, 2]]
def get_img__31(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-5"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3]]
def get_img__32(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('calibrate',instrument,state.on_board[instrument],"direc-3"),('turn_to',state.on_board[instrument],"direc-2"),('switch_off',state.on_board[instrument]),('turn_to',state.on_board[instrument],"direc-3"),('calibrate',instrument,state.on_board[instrument],"direc-3")], [[0, 1], [2, 3], [3, 4], [4, 5], [5, 6]]
def activate__28(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('turn_to',satellite,"direc-3")], []
def get_img__33(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('calibrate',instrument,state.on_board[instrument],"direc-3"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3]]
def activate__29(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('calibrate',instrument,satellite,"direc-4"),('turn_to',satellite,"direc-1"),('turn_to',satellite,"direc-4")], [[1, 2], [2, 3]]
def get_img__34(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-4"),('switch_off',"sate-2")], [[0, 1], [2, 3]]
def get_img__35(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('calibrate',instrument,state.on_board[instrument],direction),('turn_to',state.on_board[instrument],"direc-3"),('calibrate',instrument,state.on_board[instrument],direction)], [[0, 1], [2, 3], [3, 4]]
def activate__30(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('switch_off',satellite),('turn_to',satellite,direction)], [[1, 2]]
def activate__31(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('calibrate',instrument,satellite,direction),('turn_to',satellite,direction),('turn_to',satellite,direction)], [[1, 2], [2, 3]]
def get_img__36(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-4"),('switch_off',state.on_board[instrument]),('calibrate',instrument,state.on_board[instrument],direction)], [[0, 1], [2, 3], [3, 4]]
def get_img__37(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('calibrate',instrument,state.on_board[instrument],"direc-5"),('turn_to',state.on_board[instrument],direction),('switch_off',state.on_board[instrument])], [[0, 1], [2, 3], [3, 4]]
def activate__32(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('turn_to',satellite,"direc-3"),('calibrate',instrument,satellite,"direc-3")], [[1, 2]]
def activate__33(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('turn_to',satellite,direction),('switch_off',satellite),('turn_to',satellite,direction)], [[1, 2], [2, 3]]
def get_img__38(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('calibrate',instrument,state.on_board[instrument],direction),('calibrate',instrument,state.on_board[instrument],direction)], [[0, 1], [2, 3]]
def get_img__39(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('switch_off',state.on_board[instrument]),('calibrate',instrument,state.on_board[instrument],"direc-5"),('turn_to',state.on_board[instrument],"direc-5"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3], [3, 4], [4, 5]]
def activate__34(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('turn_to',satellite,"direc-5"),('switch_off',satellite),('calibrate',instrument,satellite,"direc-5")], [[1, 2], [2, 3]]
def get_img__40(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('calibrate',instrument,state.on_board[instrument],direction)], [[0, 1]]
def activate__35(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('turn_to',satellite,"direc-1"),('turn_to',satellite,direction)], [[1, 2]]
def get_img__41(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('calibrate',instrument,state.on_board[instrument],"direc-1")], [[0, 1]]
def activate__36(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('switch_off',satellite),('calibrate',instrument,satellite,"direc-4"),('turn_to',satellite,direction)], [[1, 2], [2, 3]]
def get_img__42(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('switch_off',state.on_board[instrument]),('turn_to',state.on_board[instrument],"direc-4"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3], [3, 4]]
def activate__37(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('calibrate',instrument,satellite,"direc-4")], []
def get_img__43(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-5")], [[0, 1]]
def activate__38(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('calibrate',instrument,satellite,direction),('calibrate',instrument,satellite,direction)], [[1, 2]]
def get_img__44(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],"direc-2"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3]]
def activate__39(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('calibrate',instrument,satellite,"direc-3"),('switch_off',satellite),('turn_to',satellite,"direc-3")], [[1, 2], [2, 3]]
def get_img__45(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('turn_to',state.on_board[instrument],direction),('switch_off',"sate-2")], [[0, 1], [2, 3]]
def get_img__46(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('calibrate',instrument,state.on_board[instrument],"direc-5"),('turn_to',state.on_board[instrument],direction)], [[0, 1], [2, 3]]
def get_img__47(state, direction, mode):
	instrument = state.mode[mode][0]

	return [('activate',instrument,state.on_board[instrument],direction),('take_img',state.on_board[instrument],direction,instrument,mode),('calibrate',instrument,state.on_board[instrument],"direc-4"),('switch_off',state.on_board[instrument])], [[0, 1], [2, 3]]
def activate__40(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('turn_to',satellite,"direc-2"),('turn_to',satellite,direction),('calibrate',instrument,satellite,direction)], [[1, 2], [2, 3]]
def activate__41(state, instrument, satellite, direction):

	return [('switch_on',instrument,satellite),('switch_off',satellite),('turn_to',satellite,"direc-5"),('calibrate',instrument,satellite,"direc-5")], [[1, 2], [2, 3]]
