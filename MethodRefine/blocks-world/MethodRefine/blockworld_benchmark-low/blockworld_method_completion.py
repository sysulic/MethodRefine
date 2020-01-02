import copy
import random
def tower1__1(state, block1):
	return [('pick_up',block1),('put_down',block1)], [[0, 1]]

def tower2__1(state, block1, block2):
	return [('tower1',block1),('make_clear',block2),('checkpile1',()),('pick_up',block2),('stack',block2,block1)], [[0, 1], [1, 2], [2, 3], [3, 4]]

def make_clear__1__1(state, block):
	if (state.clear[block] == False):
		block_on = state.on[block]
		return [('pick_up',block_on),('put_down',block_on)], [[0, 1]]
	else:
		return False,[]

def tower3__1(state, block1, block2, block3):
	return [('tower2',block1,block2),('make_clear',block3),('checkpile2',()),('pick_up',block3),('stack',block3,block2)], [[0, 1], [1, 2], [2, 3], [3, 4]]

def tower4__1(state, block1, block2, block3, block4):
	return [('tower3',block1,block2,block3),('make_clear',block4),('checkpile3',()),('pick_up',block4),('stack',block4,block3)], [[0, 1], [1, 2], [2, 3], [3, 4]]

def tower5__1(state, block1, block2, block3, block4, block5):
	return [('tower4',block1,block2,block3,block4),('make_clear',block5),('checkpile4',()),('pick_up',block5),('stack',block5,block4)], [[0, 1], [1, 2], [2, 3], [3, 4]]

def make_clear__1__2(state, block):
	if (state.clear[block] == False):
		block_on = state.on[block]
		return [('pick_up',"block-5"),('put_down',"block-5"),('pick_up',block_on),('put_down',block_on)], [[0, 1], [1, 2], [2, 3]]
	else:
		return False,[]

def tower1__2(state, block1):
	return [('pick_up',"block-2"),('put_down',"block-2"),('pick_up',block1),('put_down',block1)], [[0, 1], [1, 2], [2, 3]]

def tower1__3(state, block1):
	return [('pick_up',"block-3"),('put_down',"block-3"),('pick_up',"block-5"),('put_down',"block-5"),('pick_up',block1),('put_down',block1)], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]

def tower1__4(state, block1):
	return [('pick_up',"block-4"),('put_down',"block-4"),('pick_up',"block-2"),('put_down',"block-2"),('pick_up',block1),('put_down',block1)], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]

def tower1__5(state, block1):
	return [('pick_up',"block-4"),('put_down',"block-4"),('pick_up',block1),('put_down',block1)], [[0, 1], [1, 2], [2, 3]]

