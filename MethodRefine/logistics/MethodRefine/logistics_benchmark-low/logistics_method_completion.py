import copy
import random
def city_ship__1(state,pkg,goal):
	truck = 'truck' + goal[0][4:]
	return [('drive_truck',truck,(copy.deepcopy(goal[0]), 'loc' + str(3 - int(goal[1][-1])))),('load_truck',pkg,(copy.deepcopy(goal[0]), 'loc' + str(3 - int(goal[1][-1]))),truck),('drive_truck',truck,goal),('unload_truck',pkg,goal,truck)], [[0, 1], [1, 2], [2, 3]]
def city_ship__2(state,pkg,goal):
	truck = 'truck' + goal[0][4:]
	return [('load_truck',pkg,(copy.deepcopy(goal[0]), 'loc' + str(3 - int(goal[1][-1]))),truck),('drive_truck',truck,goal),('unload_truck',pkg,goal,truck)], [[0, 1], [1, 2]]
def air_ship__1(state,pkg,goal):
	i = random.randint(1, state.plane_nums)
	plane = 'plane' + str(i)
	return [('by_plane',plane,(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('drive_truck',"truck3","('city3', 'loc2')"),('load_truck',pkg,"('city3', 'loc2')","truck3"),('drive_truck',"truck3",(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('unload_truck',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),"truck3"),('load_plane',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),plane),('by_plane',plane,goal),('unload_plane',pkg,goal,plane)], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
def air_ship__2(state,pkg,goal):
	i = random.randint(1, state.plane_nums)
	plane = 'plane' + str(i)
	return [('by_plane',plane,(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('load_plane',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),plane),('by_plane',plane,goal),('unload_plane',pkg,goal,plane)], [[0, 1], [1, 2], [2, 3]]
def air_ship__3(state,pkg,goal):
	i = random.randint(1, state.plane_nums)
	plane = 'plane' + str(i)
	return [('by_plane',plane,(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('drive_truck',"truck4","('city4', 'loc2')"),('load_truck',pkg,"('city4', 'loc2')","truck4"),('drive_truck',"truck4",(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('unload_truck',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),"truck4"),('load_plane',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),plane),('by_plane',plane,goal),('unload_plane',pkg,goal,plane)], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
def air_ship__4(state,pkg,goal):
	i = random.randint(1, state.plane_nums)
	plane = 'plane' + str(i)
	return [('load_plane',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),plane),('by_plane',plane,goal),('unload_plane',pkg,goal,plane)], [[0, 1], [1, 2]]
def air_ship__5(state,pkg,goal):
	i = random.randint(1, state.plane_nums)
	plane = 'plane' + str(i)
	return [('load_truck',pkg,"('city2', 'loc2')","truck2"),('drive_truck',"truck2",(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('unload_truck',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),"truck2"),('by_plane',plane,(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('load_plane',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),plane),('by_plane',plane,goal),('unload_plane',pkg,goal,plane)], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
def air_ship__6(state,pkg,goal):
	i = random.randint(1, state.plane_nums)
	plane = 'plane' + str(i)
	return [('load_truck',pkg,"('city5', 'loc2')","truck5"),('drive_truck',"truck5",(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('unload_truck',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),"truck5"),('by_plane',plane,(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('load_plane',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),plane),('by_plane',plane,goal),('unload_plane',pkg,goal,plane)], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
def air_ship__7(state,pkg,goal):
	i = random.randint(1, state.plane_nums)
	plane = 'plane' + str(i)
	return [('load_truck',pkg,"('city1', 'loc2')","truck1"),('drive_truck',"truck1",(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('unload_truck',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),"truck1"),('by_plane',plane,(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('load_plane',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),plane),('by_plane',plane,goal),('unload_plane',pkg,goal,plane)], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
def air_ship__8(state,pkg,goal):
	i = random.randint(1, state.plane_nums)
	plane = 'plane' + str(i)
	return [('load_truck',pkg,"('city3', 'loc2')","truck3"),('drive_truck',"truck3",(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('unload_truck',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),"truck3"),('by_plane',plane,(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('load_plane',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),plane),('by_plane',plane,goal),('unload_plane',pkg,goal,plane)], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
def air_ship__9(state,pkg,goal):
	i = random.randint(1, state.plane_nums)
	plane = 'plane' + str(i)
	return [('by_plane',plane,(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('drive_truck',"truck1","('city1', 'loc2')"),('load_truck',pkg,"('city1', 'loc2')","truck1"),('drive_truck',"truck1",(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('unload_truck',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),"truck1"),('load_plane',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),plane),('by_plane',plane,goal),('unload_plane',pkg,goal,plane)], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
def air_ship__10(state,pkg,goal):
	i = random.randint(1, state.plane_nums)
	plane = 'plane' + str(i)
	return [('by_plane',plane,(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('drive_truck',"truck5","('city5', 'loc2')"),('load_truck',pkg,"('city5', 'loc2')","truck5"),('drive_truck',"truck5",(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('unload_truck',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),"truck5"),('load_plane',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),plane),('by_plane',plane,goal),('unload_plane',pkg,goal,plane)], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
def air_ship__11(state,pkg,goal):
	i = random.randint(1, state.plane_nums)
	plane = 'plane' + str(i)
	return [('by_plane',plane,(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('drive_truck',"truck2","('city2', 'loc2')"),('load_truck',pkg,"('city2', 'loc2')","truck2"),('drive_truck',"truck2",(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('unload_truck',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),"truck2"),('load_plane',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),plane),('by_plane',plane,goal),('unload_plane',pkg,goal,plane)], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
def air_ship__12(state,pkg,goal):
	i = random.randint(1, state.plane_nums)
	plane = 'plane' + str(i)
	return [('load_truck',pkg,"('city4', 'loc2')","truck4"),('drive_truck',"truck4",(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('unload_truck',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),"truck4"),('load_plane',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),plane),('by_plane',plane,goal),('unload_plane',pkg,goal,plane)], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]
def air_ship__13(state,pkg,goal):
	i = random.randint(1, state.plane_nums)
	plane = 'plane' + str(i)
	return [('drive_truck',"truck1","('city1', 'loc2')"),('load_truck',pkg,"('city1', 'loc2')","truck1"),('drive_truck',"truck1",(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('unload_truck',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),"truck1"),('load_plane',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),plane),('by_plane',plane,goal),('unload_plane',pkg,goal,plane)], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
def air_ship__14(state,pkg,goal):
	i = random.randint(1, state.plane_nums)
	plane = 'plane' + str(i)
	return [('load_truck',pkg,"('city5', 'loc2')","truck5"),('drive_truck',"truck5",(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('unload_truck',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),"truck5"),('load_plane',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),plane),('by_plane',plane,goal),('unload_plane',pkg,goal,plane)], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]
def air_ship__15(state,pkg,goal):
	i = random.randint(1, state.plane_nums)
	plane = 'plane' + str(i)
	return [('load_truck',pkg,"('city4', 'loc2')","truck4"),('drive_truck',"truck4",(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('unload_truck',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),"truck4"),('by_plane',plane,(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('load_plane',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),plane),('by_plane',plane,goal),('unload_plane',pkg,goal,plane)], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
def air_ship__16(state,pkg,goal):
	i = random.randint(1, state.plane_nums)
	plane = 'plane' + str(i)
	return [('load_truck',pkg,"('city2', 'loc2')","truck2"),('drive_truck',"truck2",(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('unload_truck',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),"truck2"),('load_plane',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),plane),('by_plane',plane,goal),('unload_plane',pkg,goal,plane)], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]
def air_ship__17(state,pkg,goal):
	i = random.randint(1, state.plane_nums)
	plane = 'plane' + str(i)
	return [('load_truck',pkg,"('city1', 'loc2')","truck1"),('drive_truck',"truck1",(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('unload_truck',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),"truck1"),('load_plane',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),plane),('by_plane',plane,goal),('unload_plane',pkg,goal,plane)], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]
