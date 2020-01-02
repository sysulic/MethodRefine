import copy
import random
def tower5__1(state, block1, block2, block3, block4, block5):

	
	return [('tower4',block1,block2,block3,block4),('make_clear',block5),('checkpile4',()),('pick_up',block5),('stack',block5,block4),('pick_up',block2),('put_down',block2),('pick_up',block2)], [[0, 1], [1, 2], [2, 3], [3, 4], [5, 6], [6, 7]]
def tower2__1(state, block1, block2):

	
	return [('tower1',block1),('make_clear',block2),('checkpile1',()),('stack',block2,block1),('pick_up',block1)], [[0, 1], [1, 2], [2, 3]]
def tower2__2(state, block1, block2):

	
	return [('tower1',block1),('make_clear',block2),('checkpile1',()),('stack',block2,block1),('pick_up',block2),('pick_up',block2)], [[0, 1], [1, 2], [2, 3], [4, 5]]
def tower3__1(state, block1, block2, block3):

	
	return [('tower2',block1,block2),('make_clear',block3),('checkpile2',()),('pick_up',block3),('stack',block3,block2),('put_down',block2),('pick_up',block1)], [[0, 1], [1, 2], [2, 3], [3, 4], [5, 6]]
def tower5__2(state, block1, block2, block3, block4, block5):

	
	return [('tower4',block1,block2,block3,block4),('make_clear',block5),('checkpile4',()),('pick_up',block5),('stack',block5,block4),('pick_up',block3),('pick_up',block5),('put_down',block5)], [[0, 1], [1, 2], [2, 3], [3, 4], [5, 6], [6, 7]]
def tower1__1(state, block1):

	
	return [('put_down',block1),('put_down',"block-3"),('pick_up',block1)], [[1, 2]]
def tower3__2(state, block1, block2, block3):

	
	return [('tower2',block1,block2),('make_clear',block3),('checkpile2',()),('pick_up',block3),('stack',block3,block2),('pick_up',block2)], [[0, 1], [1, 2], [2, 3], [3, 4]]
def tower2__3(state, block1, block2):

	
	return [('tower1',block1),('make_clear',block2),('checkpile1',()),('stack',block2,block1),('pick_up',"block-4")], [[0, 1], [1, 2], [2, 3]]
def tower1__2(state, block1):

	
	return [('put_down',block1),('put_down',"block-4")], []
def tower4__1(state, block1, block2, block3, block4):

	
	return [('tower3',block1,block2,block3),('make_clear',block4),('checkpile3',()),('pick_up',block4),('stack',block4,block3),('pick_up',block1)], [[0, 1], [1, 2], [2, 3], [3, 4]]
def tower5__3(state, block1, block2, block3, block4, block5):

	
	return [('tower4',block1,block2,block3,block4),('make_clear',block5),('checkpile4',()),('pick_up',block5),('stack',block5,block4),('pick_up',block2)], [[0, 1], [1, 2], [2, 3], [3, 4]]
def tower2__4(state, block1, block2):

	
	return [('tower1',block1),('make_clear',block2),('checkpile1',()),('stack',block2,block1),('pick_up',"block-4"),('put_down',"block-4")], [[0, 1], [1, 2], [2, 3], [4, 5]]
def tower5__4(state, block1, block2, block3, block4, block5):

	
	return [('tower4',block1,block2,block3,block4),('make_clear',block5),('checkpile4',()),('pick_up',block5),('stack',block5,block4),('pick_up',block1)], [[0, 1], [1, 2], [2, 3], [3, 4]]
def tower4__2(state, block1, block2, block3, block4):

	
	return [('tower3',block1,block2,block3),('make_clear',block4),('checkpile3',()),('pick_up',block4),('stack',block4,block3),('pick_up',block2)], [[0, 1], [1, 2], [2, 3], [3, 4]]
def tower4__3(state, block1, block2, block3, block4):

	
	return [('tower3',block1,block2,block3),('make_clear',block4),('checkpile3',()),('pick_up',block4),('stack',block4,block3),('pick_up',block1),('pick_up',block2)], [[0, 1], [1, 2], [2, 3], [3, 4], [5, 6]]
