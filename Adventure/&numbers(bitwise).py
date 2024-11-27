import display
from display import Display as base

models = [base(6,5),base(6,5),base(6,5),base(6,5),base(6,5),base(6,5),base(6,5),base(6,5),base(6,5),base(6,5),]

models[0].row_turn(1)
models[0].row_turn(6)
models[0].column_turn(1)
models[0].column_turn(5)
models[0].turn(2,4)
models[0].turn(3,3)
models[0].turn(4,3)
models[0].turn(5,2)

models[1].column_turn(3)
models[1].turn(2,2)
models[1].turn(6,2)
models[1].turn(6,4)

models[2].row_turn(1)
models[2].row_turn(6)
models[2].turn(1,1)
models[2].turn(1,5)
models[2].turn(2,1)
models[2].turn(2,5)
models[2].turn(3,4)
models[2].turn(4,3)
models[2].turn(5,2)

models[3].row_turn(1)
models[3].turn(2,5)
models[3].turn(3,4)
models[3].turn(3,3)
models[3].turn(4,5)
models[3].turn(5,5)
models[3].turn(5,1)
models[3].turn(6,2)
models[3].turn(6,3)
models[3].turn(6,4)

models[4].row_turn(5)
models[4].column_turn(4)
models[4].turn(5,4)
models[4].turn(2,3)
models[4].turn(3,2)
models[4].turn(4,1)

models[5].row_turn(1)
models[5].row_turn(3)
models[5].turn(2,1)
models[5].turn(3,5)
models[5].turn(4,5)
models[5].turn(5,5)
models[5].turn(5,1)
models[5].turn(6,2)
models[5].turn(6,3)
models[5].turn(6,4)

models[6].row_turn(3)
models[6].turn(1,2)
models[6].turn(1,3)
models[6].turn(1,4)
models[6].turn(2,1)
models[6].turn(3,5)
models[6].turn(4,1)
models[6].turn(4,5)
models[6].turn(5,1)
models[6].turn(5,5)
models[6].turn(6,2)
models[6].turn(6,3)
models[6].turn(6,4)

models[7].row_turn(1)
models[7].turn(2,5)
models[7].turn(3,4)
models[7].turn(4,3)
models[7].turn(5,3)
models[7].turn(6,3)

models[8].tile_turn(1,2,1,4)
models[8].tile_turn(3,2,3,4)
models[8].tile_turn(6,2,6,4)
models[8].tile_turn(4,1,5,5)
models[8].tile_turn(4,2,5,4)
models[8].turn(2,1)
models[8].turn(2,5)

models[9].tile_turn(1,2,1,4)
models[9].tile_turn(4,2,4,4)
models[9].tile_turn(6,2,6,4)
models[9].tile_turn(2,1,3,1)
models[9].tile_turn(2,5,5,5)

def magnified(num):
    n = str(num)
    result = ""
    for i in n:
        result = result + models[int(i)].get()
    return result
    
print(magnified(56))
