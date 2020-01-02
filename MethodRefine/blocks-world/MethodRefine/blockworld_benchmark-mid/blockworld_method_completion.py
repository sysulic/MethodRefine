import copy
import random
def tower2__1(state, block1, block2):
	return [('tower1',block1),('make_clear',block2),('checkpile1',()),('pick_up',block2),('stack',block2,block1)], [[0, 1], [1, 2], [2, 3], [3, 4]]

def tower3__1(state, block1, block2, block3):
	return [('tower2',block1,block2),('make_clear',block3),('checkpile2',()),('pick_up',"block-5"),('put_down',"block-5"),('pick_up',block3),('stack',block3,block2)], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]

def tower4__1(state, block1, block2, block3, block4):
	return [('tower3',block1,block2,block3),('make_clear',block4),('checkpile3',()),('pick_up',block4),('stack',block4,block3)], [[0, 1], [1, 2], [2, 3], [3, 4]]

def tower1__1(state, block1):
	return [('make_clear',block1),('pick_up',block1),('put_down',block1)], [[0, 1], [1, 2]]

def tower5__1(state, block1, block2, block3, block4, block5):
	return [('tower4',block1,block2,block3,block4),('make_clear',block5),('checkpile4',()),('pick_up',block5),('stack',block5,block4)], [[0, 1], [1, 2], [2, 3], [3, 4]]

def tower2__2(state, block1, block2):
	return [('tower1',block1),('make_clear',block2),('checkpile1',()),('pick_up',"block-5"),('put_down',"block-5"),('pick_up',"block-3"),('put_down',"block-3"),('pick_up',block2),('stack',block2,block1)], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]

def tower3__2(state, block1, block2, block3):
	return [('tower2',block1,block2),('make_clear',block3),('checkpile2',()),('pick_up',block3),('stack',block3,block2)], [[0, 1], [1, 2], [2, 3], [3, 4]]

def tower4__2(state, block1, block2, block3, block4):
	return [('tower3',block1,block2,block3),('make_clear',block4),('checkpile3',()),('pick_up',"block-5"),('stack',"block-5",block3),('pick_up',block4),('put_down',block4),('pick_up',"block-5"),('put_down',"block-5"),('pick_up',block4),('stack',block4,block3)], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]

def tower1__2(state, block1):
	return [('make_clear',block1),('pick_up',"block-2"),('put_down',"block-2"),('pick_up',block1),('put_down',block1)], [[0, 1], [1, 2], [2, 3], [3, 4]]

def tower1__3(state, block1):
	return [('make_clear',block1),('pick_up',"block-3"),('put_down',"block-3"),('pick_up',"block-5"),('put_down',"block-5"),('pick_up',block1),('put_down',block1)], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]

def tower1__4(state, block1):
	return [('make_clear',block1),('pick_up',"block-4"),('put_down',"block-4"),('pick_up',"block-2"),('put_down',"block-2"),('pick_up',block1),('put_down',block1)], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]

def tower1__5(state, block1):
	return [('make_clear',block1),('pick_up',"block-4"),('put_down',"block-4"),('pick_up',block1),('put_down',block1)], [[0, 1], [1, 2], [2, 3], [3, 4]]

def tower2__3(state, block1, block2):
	return [('tower1',block1),('make_clear',block2),('checkpile1',()),('pick_up',"block-5"),('put_down',"block-5"),('pick_up',block2),('stack',block2,block1)], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]

def tower2__4(state, block1, block2):
	return [('tower1',block1),('make_clear',block2),('checkpile1',()),('pick_up',"block-3"),('put_down',"block-3"),('pick_up',block2),('stack',block2,block1)], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]

def tower1__6(state, block1):
	return [('make_clear',block1),('pick_up',"block-5"),('put_down',"block-5"),('pick_up',block1),('put_down',block1)], [[0, 1], [1, 2], [2, 3], [3, 4]]

def tower3__3(state, block1, block2, block3):
	return [('tower2',block1,block2),('make_clear',block3),('checkpile2',()),('pick_up',"block-4"),('stack',"block-4",block2),('pick_up',"block-5"),('stack',"block-5","block-4"),('pick_up',block3),('put_down',block3),('pick_up',"block-5"),('put_down',"block-5"),('pick_up',"block-4"),('put_down',"block-4"),('pick_up',block3),('stack',block3,block2)], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]

def tower3__4(state, block1, block2, block3):
	return [('tower2',block1,block2),('make_clear',block3),('checkpile2',()),('pick_up',"block-4"),('put_down',"block-4"),('pick_up',block3),('stack',block3,block2)], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]

def tower1__7(state, block1):
	return [('make_clear',block1),('pick_up',"block-3"),('put_down',"block-3"),('pick_up',block1),('put_down',block1)], [[0, 1], [1, 2], [2, 3], [3, 4]]

def tower2__5(state, block1, block2):
	return [('tower1',block1),('make_clear',block2),('checkpile1',()),('pick_up',"block-4"),('put_down',"block-4"),('pick_up',block2),('stack',block2,block1)], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]

def tower1__8(state, block1):
	return [('make_clear',block1),('pick_up',"block-2"),('put_down',"block-2"),('pick_up',"block-3"),('put_down',"block-3"),('pick_up',block1),('put_down',block1)], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]

def tower3__5(state, block1, block2, block3):
	return [('tower2',block1,block2),('make_clear',block3),('checkpile2',()),('pick_up',"block-5"),('stack',"block-5",block2),('pick_up',"block-4"),('stack',"block-4","block-5"),('pick_up',block3),('put_down',block3),('pick_up',"block-4"),('put_down',"block-4"),('pick_up',"block-5"),('put_down',"block-5"),('pick_up',block3),('stack',block3,block2)], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14]]

