import new_tihtn_planner
import random
import copy

# define the operators
def turn_to(state, satellite, direction):
	if (state.pointing[satellite] != direction):
		state.pointing[satellite] = direction
		return state
	else:
		return False

def switch_on(state, instrument, satellite):
	if (state.on_board[instrument] == satellite and state.power_avail[satellite] == True):
		state.power_on[instrument] = True
		state.calibrate[instrument] = False
		state.power_avail[satellite] = False
		return state
	else:
		return False

def switch_off(state, satellite):
	for inst in state.on_board[satellite]:
		state.power_on[inst] = False
		state.power_avail[satellite] = True
		return state

def calibrate(state, instrument, satellite, direction):
	if (state.on_board[instrument] == satellite and state.calib_target[instrument] == direction and state.pointing[satellite] == direction and state.power_on[instrument] == True and state.calibrate[instrument] == False):
		state.calibrate[instrument] = True
		return state
	else:
		return False

def take_img(state, satellite, direction, instrument, mode):
	if (state.calibrate[instrument] == True and state.on_board[instrument] == satellite and state.mode[instrument] == mode and state.power_on[instrument] == True and state.pointing[satellite] == direction):
		state.have_img[direction][mode] = True
		return state
	else:
		return False

new_tihtn_planner.declare_operators(turn_to, switch_on, switch_off, calibrate, take_img)
print('')
new_tihtn_planner.print_operators()

# define the methods
def get_img(state, direction, mode):
	instrument = state.mode[mode][0]
	return [('activate', instrument, state.on_board[instrument], direction), ('take_img', state.on_board[instrument], direction, instrument, mode)], [[0, 1]]

def activate(state, instrument, satellite, direction):
	# return [('switch_off', satellite), ('switch_on', instrument, satellite), ('auto_calibrate', instrument)], [[0, 1],[1, 2]]
	return [('switch_on', instrument, satellite)], []

# def auto_calibrate(state, instrument):
# 	return [('calibrate', instrument, state.on_board[instrument], state.calib_target[instrument])], []

new_tihtn_planner.declare_methods('get_img',get_img)
new_tihtn_planner.declare_methods('activate',activate)
# new_tihtn_planner.declare_methods('auto_calibrate', auto_calibrate)

new_tihtn_planner.print_methods()