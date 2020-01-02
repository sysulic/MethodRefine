import copy
import random
def air_ship__1(state,pkg,goal):
	i = random.randint(1, state.plane_nums)
	plane = 'plane' + str(i)
	return [('by_plane',plane,(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('load_plane',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),plane),('by_plane',plane,goal),('unload_plane',pkg,goal,plane)], [[0, 1], [1, 2], [2, 3]]
def city_ship__1(state,pkg,goal):
	truck = 'truck' + goal[0][4:]
	return [('load_truck',pkg,(copy.deepcopy(goal[0]), 'loc' + str(3 - int(goal[1][-1]))),truck),('drive_truck',truck,goal),('unload_truck',pkg,goal,truck)], [[0, 1], [1, 2]]
def city_ship__2(state,pkg,goal):
	truck = 'truck' + goal[0][4:]
	return [('drive_truck',truck,(copy.deepcopy(goal[0]), 'loc' + str(3 - int(goal[1][-1])))),('load_truck',pkg,(copy.deepcopy(goal[0]), 'loc' + str(3 - int(goal[1][-1]))),truck),('drive_truck',truck,goal),('unload_truck',pkg,goal,truck)], [[0, 1], [1, 2], [2, 3]]
def air_ship__2(state,pkg,goal):
	i = random.randint(1, state.plane_nums)
	plane = 'plane' + str(i)
	return [('load_plane',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),plane),('by_plane',plane,goal),('unload_plane',pkg,goal,plane)], [[0, 1], [1, 2]]
