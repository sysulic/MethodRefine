import copy
import random
def delievery__1(state,pkg,goal):

	return [('air_ship',pkg,('city4', 'loc1')),('city_ship',pkg,goal),('by_plane',"plane1",('city5', 'loc1')),('unload_truck',pkg,('city5', 'loc1'),"truck5"),('by_plane',"plane1",('city4', 'loc1')),('drive_truck',"truck4",goal)], [[0, 1], [2, 3], [3, 4], [4, 5]]
def air_ship__1(state,pkg,goal):
	i = random.randint(1, state.plane_nums)
	plane = 'plane' + str(i)
	return [('load_plane',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),plane),('unload_plane',pkg,goal,plane),('drive_truck',"truck5",('city5', 'loc2')),('load_truck',pkg,('city5', 'loc2'),"truck5"),('drive_truck',"truck5",(copy.deepcopy(state.loc[pkg][0]), 'loc1'))], [[0, 1], [2, 3], [3, 4]]
def air_ship__2(state,pkg,goal):
	i = random.randint(1, state.plane_nums)
	plane = 'plane' + str(i)
	return [('load_plane',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),plane),('unload_plane',pkg,goal,plane),('by_plane',plane,(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('by_plane',plane,goal)], [[0, 1], [2, 3]]
def city_ship__1(state,pkg,goal):
	truck = 'truck' + goal[0][4:]
	return [('load_truck',pkg,(copy.deepcopy(goal[0]), 'loc' + str(3 - int(goal[1][-1]))),truck),('unload_truck',pkg,goal,truck),('drive_truck',truck,goal)], [[0, 1]]
def delievery__2(state,pkg,goal):

	return [('city_ship',pkg,goal),('drive_truck',"truck2",('city2', 'loc2'))], []
def city_ship__2(state,pkg,goal):
	truck = 'truck' + goal[0][4:]
	return [('load_truck',pkg,(copy.deepcopy(goal[0]), 'loc' + str(3 - int(goal[1][-1]))),truck),('unload_truck',pkg,goal,truck),('drive_truck',truck,goal),('by_plane',"plane1",goal)], [[0, 1], [2, 3]]
def air_ship__3(state,pkg,goal):
	i = random.randint(1, state.plane_nums)
	plane = 'plane' + str(i)
	return [('load_plane',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),plane),('unload_plane',pkg,goal,plane),('by_plane',plane,goal)], [[0, 1]]
def city_ship__3(state,pkg,goal):
	truck = 'truck' + goal[0][4:]
	return [('load_truck',pkg,(copy.deepcopy(goal[0]), 'loc' + str(3 - int(goal[1][-1]))),truck),('unload_truck',pkg,goal,truck),('drive_truck',truck,(copy.deepcopy(goal[0]), 'loc' + str(3 - int(goal[1][-1])))),('drive_truck',truck,goal)], [[0, 1], [2, 3]]
def delievery__3(state,pkg,goal):

	return [('city_ship',pkg,('city5', 'loc1')),('air_ship',pkg,goal),('drive_truck',"truck5",('city5', 'loc1')),('by_plane',"plane1",goal)], [[0, 1], [2, 3]]
def air_ship__4(state,pkg,goal):
	i = random.randint(1, state.plane_nums)
	plane = 'plane' + str(i)
	return [('load_plane',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),plane),('unload_plane',pkg,goal,plane),('by_plane',plane,(copy.deepcopy(state.loc[pkg][0]), 'loc1'))], [[0, 1]]
def delievery__4(state,pkg,goal):

	return [('city_ship',pkg,('city3', 'loc1')),('air_ship',pkg,goal),('by_plane',"plane1",('city3', 'loc1')),('by_plane',"plane1",('city3', 'loc1'))], [[0, 1], [2, 3]]
def air_ship__5(state,pkg,goal):
	i = random.randint(1, state.plane_nums)
	plane = 'plane' + str(i)
	return [('load_plane',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),plane),('unload_plane',pkg,goal,plane),('by_plane',plane,goal),('drive_truck',"truck3",(copy.deepcopy(state.loc[pkg][0]), 'loc1'))], [[0, 1], [2, 3]]
def air_ship__6(state,pkg,goal):
	i = random.randint(1, state.plane_nums)
	plane = 'plane' + str(i)
	return [('load_plane',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),plane),('unload_plane',pkg,goal,plane),('drive_truck',"truck3",('city3', 'loc2')),('by_plane',plane,goal)], [[0, 1], [2, 3]]
def delievery__5(state,pkg,goal):

	return [('air_ship',pkg,('city1', 'loc1')),('city_ship',pkg,goal),('load_truck',pkg,('city3', 'loc2'),"truck3"),('unload_truck',pkg,('city3', 'loc1'),"truck3")], [[0, 1], [2, 3]]
def city_ship__4(state,pkg,goal):
	truck = 'truck' + goal[0][4:]
	return [('load_truck',pkg,(copy.deepcopy(goal[0]), 'loc' + str(3 - int(goal[1][-1]))),truck),('unload_truck',pkg,goal,truck),('drive_truck',truck,(copy.deepcopy(goal[0]), 'loc' + str(3 - int(goal[1][-1])))),('by_plane',"plane1",goal)], [[0, 1], [2, 3]]
def delievery__6(state,pkg,goal):

	return [('city_ship',pkg,('city3', 'loc1')),('air_ship',pkg,goal),('drive_truck',"truck3",('city3', 'loc1')),('by_plane',"plane1",goal)], [[0, 1], [2, 3]]
def city_ship__5(state,pkg,goal):
	truck = 'truck' + goal[0][4:]
	return [('load_truck',pkg,(copy.deepcopy(goal[0]), 'loc' + str(3 - int(goal[1][-1]))),truck),('unload_truck',pkg,goal,truck),('drive_truck',truck,(copy.deepcopy(goal[0]), 'loc' + str(3 - int(goal[1][-1]))))], [[0, 1]]
def delievery__7(state,pkg,goal):

	return [('city_ship',pkg,('city3', 'loc1')),('air_ship',pkg,goal),('drive_truck',"truck3",('city3', 'loc1')),('by_plane',"plane1",('city2', 'loc1'))], [[0, 1], [2, 3]]
def delievery__8(state,pkg,goal):

	return [('air_ship',pkg,('city5', 'loc1')),('city_ship',pkg,goal),('by_plane',"plane1",('city5', 'loc1'))], [[0, 1]]
def delievery__9(state,pkg,goal):

	return [('city_ship',pkg,goal),('drive_truck',"truck5",goal)], []
def delievery__10(state,pkg,goal):

	return [('air_ship',pkg,('city5', 'loc1')),('city_ship',pkg,goal),('load_truck',pkg,('city1', 'loc2'),"truck1"),('drive_truck',"truck1",('city1', 'loc1')),('unload_truck',pkg,('city1', 'loc1'),"truck1"),('by_plane',"plane1",('city5', 'loc1')),('drive_truck',"truck5",('city5', 'loc1'))], [[0, 1], [2, 3], [3, 4], [4, 5], [5, 6]]
def air_ship__7(state,pkg,goal):
	i = random.randint(1, state.plane_nums)
	plane = 'plane' + str(i)
	return [('load_plane',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),plane),('unload_plane',pkg,goal,plane),('by_plane',plane,(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('drive_truck',"truck5",goal)], [[0, 1], [2, 3]]
def delievery__11(state,pkg,goal):

	return [('air_ship',pkg,goal),('by_plane',"plane1",('city3', 'loc1')),('by_plane',"plane1",goal)], [[1, 2]]
def delievery__12(state,pkg,goal):

	return [('air_ship',pkg,goal),('by_plane',"plane1",('city4', 'loc1')),('by_plane',"plane1",goal)], [[1, 2]]
def city_ship__6(state,pkg,goal):
	truck = 'truck' + goal[0][4:]
	return [('load_truck',pkg,(copy.deepcopy(goal[0]), 'loc' + str(3 - int(goal[1][-1]))),truck),('unload_truck',pkg,goal,truck),('drive_truck',truck,goal),('drive_truck',truck,(copy.deepcopy(goal[0]), 'loc' + str(3 - int(goal[1][-1])))),('by_plane',"plane1",(copy.deepcopy(goal[0]), 'loc' + str(3 - int(goal[1][-1]))))], [[0, 1], [2, 3], [3, 4]]
def air_ship__8(state,pkg,goal):
	i = random.randint(1, state.plane_nums)
	plane = 'plane' + str(i)
	return [('load_plane',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),plane),('unload_plane',pkg,goal,plane),('load_truck',pkg,('city4', 'loc2'),"truck4"),('by_plane',plane,goal)], [[0, 1], [2, 3]]
def delievery__13(state,pkg,goal):

	return [('city_ship',pkg,goal),('unload_truck',"pkg3",('city4', 'loc1'),"truck4")], []
def city_ship__7(state,pkg,goal):
	truck = 'truck' + goal[0][4:]
	return [('load_truck',pkg,(copy.deepcopy(goal[0]), 'loc' + str(3 - int(goal[1][-1]))),truck),('unload_truck',pkg,goal,truck),('drive_truck',truck,goal),('by_plane',"plane1",('city4', 'loc1')),('drive_truck',"truck4",('city4', 'loc1')),('unload_truck',"pkg4",('city4', 'loc1'),"truck4")], [[0, 1], [2, 3], [3, 4], [4, 5]]
def delievery__14(state,pkg,goal):

	return [('air_ship',pkg,('city3', 'loc1')),('city_ship',pkg,goal),('drive_truck',"truck4",('city4', 'loc2')),('by_plane',"plane1",('city3', 'loc1'))], [[0, 1], [2, 3]]
def air_ship__9(state,pkg,goal):
	i = random.randint(1, state.plane_nums)
	plane = 'plane' + str(i)
	return [('load_plane',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),plane),('unload_plane',pkg,goal,plane),('load_truck',pkg,('city4', 'loc2'),"truck4"),('drive_truck',"truck3",goal)], [[0, 1], [2, 3]]
def delievery__15(state,pkg,goal):

	return [('air_ship',pkg,('city2', 'loc1')),('city_ship',pkg,goal),('by_plane',"plane1",('city2', 'loc1')),('by_plane',"plane1",('city4', 'loc1'))], [[0, 1], [2, 3]]
def delievery__16(state,pkg,goal):

	return [('air_ship',pkg,('city2', 'loc1')),('city_ship',pkg,goal),('by_plane',"plane1",('city2', 'loc1')),('drive_truck',"truck2",('city2', 'loc1')),('drive_truck',"truck2",goal),('drive_truck',"truck5",('city5', 'loc2'))], [[0, 1], [2, 3], [3, 4], [4, 5]]
def delievery__17(state,pkg,goal):

	return [('city_ship',pkg,('city5', 'loc1')),('air_ship',pkg,goal),('drive_truck',"truck5",('city5', 'loc1'))], [[0, 1]]
def delievery__18(state,pkg,goal):

	return [('air_ship',pkg,('city2', 'loc1')),('city_ship',pkg,goal),('by_plane',"plane1",('city1', 'loc1')),('by_plane',"plane1",('city2', 'loc1'))], [[0, 1], [2, 3]]
def delievery__19(state,pkg,goal):

	return [('air_ship',pkg,goal),('by_plane',"plane1",('city4', 'loc1'))], []
def air_ship__10(state,pkg,goal):
	i = random.randint(1, state.plane_nums)
	plane = 'plane' + str(i)
	return [('load_plane',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),plane),('unload_plane',pkg,goal,plane),('by_plane',plane,goal),('by_plane',plane,(copy.deepcopy(state.loc[pkg][0]), 'loc1'))], [[0, 1], [2, 3]]
def delievery__20(state,pkg,goal):

	return [('air_ship',pkg,('city3', 'loc1')),('city_ship',pkg,goal),('by_plane',"plane1",('city3', 'loc1')),('drive_truck',"truck3",goal)], [[0, 1], [2, 3]]
def delievery__21(state,pkg,goal):

	return [('city_ship',pkg,goal),('drive_truck',"truck3",goal)], []
def delievery__22(state,pkg,goal):

	return [('air_ship',pkg,('city5', 'loc1')),('city_ship',pkg,goal),('load_truck',pkg,('city1', 'loc2'),"truck1"),('drive_truck',"truck1",('city1', 'loc1')),('unload_truck',pkg,('city1', 'loc1'),"truck1"),('drive_truck',"truck5",('city5', 'loc1')),('drive_truck',"truck5",goal)], [[0, 1], [2, 3], [3, 4], [4, 5], [5, 6]]
def delievery__23(state,pkg,goal):

	return [('city_ship',pkg,('city2', 'loc1')),('air_ship',pkg,goal),('by_plane',"plane1",('city2', 'loc1'))], [[0, 1]]
def delievery__24(state,pkg,goal):

	return [('city_ship',pkg,goal),('drive_truck',"truck5",goal),('drive_truck',"truck3",('city3', 'loc1'))], [[1, 2]]
def city_ship__8(state,pkg,goal):
	truck = 'truck' + goal[0][4:]
	return [('load_truck',pkg,(copy.deepcopy(goal[0]), 'loc' + str(3 - int(goal[1][-1]))),truck),('unload_truck',pkg,goal,truck),('drive_truck',truck,goal),('load_truck',"pkg2",('city4', 'loc2'),"truck4")], [[0, 1], [2, 3]]
def air_ship__11(state,pkg,goal):
	i = random.randint(1, state.plane_nums)
	plane = 'plane' + str(i)
	return [('load_plane',pkg,(copy.deepcopy(state.loc[pkg][0]), 'loc1'),plane),('unload_plane',pkg,goal,plane),('by_plane',plane,(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('drive_truck',"truck4",(copy.deepcopy(state.loc[pkg][0]), 'loc1')),('drive_truck',"truck1",goal)], [[0, 1], [2, 3], [3, 4]]
def delievery__25(state,pkg,goal):

	return [('air_ship',pkg,('city2', 'loc1')),('city_ship',pkg,goal),('drive_truck',"truck4",('city4', 'loc2'))], [[0, 1]]
def delievery__26(state,pkg,goal):

	return [('air_ship',pkg,('city1', 'loc1')),('city_ship',pkg,goal),('unload_truck',pkg,('city4', 'loc1'),"truck4"),('by_plane',"plane1",('city1', 'loc1')),('drive_truck',"truck1",goal)], [[0, 1], [2, 3], [3, 4]]
def delievery__27(state,pkg,goal):

	return [('air_ship',pkg,goal),('by_plane',"plane1",goal)], []
