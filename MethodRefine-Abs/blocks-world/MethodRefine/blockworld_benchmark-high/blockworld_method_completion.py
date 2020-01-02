import copy
import random
def tower5__1(state, block1, block2, block3, block4, block5):

	
	return [('tower4',block1,block2,block3,block4),('make_clear',block5),('checkpile4',()),('pick_up',block5),('stack',block5,block4),('pick_up',block1),('pick_up',block2)], [[0, 1], [1, 2], [2, 3], [3, 4], [5, 6]]
