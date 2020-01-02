import new_tihtn_planner
import random
import copy

def pick_up(state, block):
    if (state.clear[block] == True and state.holding == False):
        state.clear[block] = False
        state.holding = block
        if (state.on_table[block] == False):
            state.on[state.down[block]] = False
            state.clear[state.down[block]] = True
            state.down[block] = False
        else:
            state.on_table[block] = False
        return state
    else:
        return False

def pick_up_from_block(state, block, block2):
    if (state.clear[block] == True and state.holding == False and state.on[block] == block2):
        state.clear[block] = False
        state.holding = block
        if (state.on_table[block] == False):
            state.on[state.down[block]] = False
            state.clear[state.down[block]] = True
            state.down[block] = False
        else:
            state.on_table[block] = False
        return state
    else:
        return False

def put_down(state, block):
    if (state.holding == block):
        state.holding = False
        state.on_table[block] = True
        state.clear[block] = True
        return state
    else:
        return False

def stack(state, block_up, block_down):
    if (state.holding == block_up and state.clear[block_down] == True):
        state.holding = False
        state.on[block_down] = block_up
        state.down[block_up] = block_down
        state.clear[block_up] = True
        state.clear[block_down] = False
        return state
    else:
        return False

def checkpile1(state, nothing):
    if (state.on_table['block-1'] == True and state.clear['block-1'] == True):
        return state
    else:
        return False

def checkpile2(state, nothing):
    if (state.on_table['block-1'] == True and state.on['block-1'] == 'block-2' and state.clear['block-2'] == True):
        return state
    else:
        return False

def checkpile3(state, nothing):
    if (state.on_table['block-1'] == True and state.on['block-1'] == 'block-2' and state.on['block-2'] == 'block-3' and state.clear['block-3'] == True):
        return state
    else:
        return False

def checkpile4(state, nothing):
    if (state.on_table['block-1'] == True and state.on['block-1'] == 'block-2' and state.on['block-2'] == 'block-3'and state.on['block-3'] == 'block-4' and state.clear['block-4'] == True):
        return state
    else:
        return False

new_tihtn_planner.declare_operators(pick_up, put_down, stack, checkpile1, checkpile2, checkpile3, checkpile4)
print('')
new_tihtn_planner.print_operators()

def tower5(state, block1, block2, block3, block4, block5):
    return [('tower4', block1, block2, block3, block4), ('make_clear', block5), ('checkpile4',()), ('pick_up', block5), ('stack', block5, block4)],[[0,1], [1,2], [2,3], [3,4]]

def tower4(state, block1, block2, block3, block4):
    return [('tower3', block1, block2, block3), ('make_clear', block4), ('checkpile3',()), ('pick_up', block4), ('stack', block4, block3)],[[0,1], [1,2], [2,3],[3,4]]

def tower3(state, block1, block2, block3):
    return [('tower2', block1, block2), ('make_clear', block3), ('checkpile2',()), ('pick_up', block3), ('stack', block3, block2)],[[0,1], [1,2], [2,3],[3,4]]

def tower2(state, block1, block2):
    return [('tower1', block1), ('make_clear', block2), ('checkpile1',()), ('stack', block2, block1)],[[0,1], [1,2], [2,3]]

def tower1(state, block1):
    return [('make_clear', block1), ('put_down', block1)],[[0,1]]

def make_clear__1(state, block):
    if (state.clear[block] == False):
        block_on = state.on[block]
        return [('make_clear', block_on), ('pick_up', block_on), ('put_down', block_on)], [[0,1],[1,2]]
    else:
        return False,[]

def make_clear__2(state, block):
    if (state.clear[block] == True):
        return [],[]
    else:
        return False,[]


new_tihtn_planner.declare_methods('tower5',tower5)
new_tihtn_planner.declare_methods('tower4',tower4)
new_tihtn_planner.declare_methods('tower3',tower3)
new_tihtn_planner.declare_methods('tower2',tower2)
new_tihtn_planner.declare_methods('tower1',tower1)
new_tihtn_planner.declare_methods('make_clear',make_clear__1, make_clear__2)

new_tihtn_planner.declare_priority({'tower5':2, 'tower4':2, 'tower3':2, 'tower2':2, 'tower1':2, 'make_clear':1})

new_tihtn_planner.print_methods()

