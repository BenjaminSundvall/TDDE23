def new_board():
    return({})

def is_free(board, column, row):
    return(not (column, row) in board) 

def place_piece(board, column, row, player):
    if is_free(board, column, row):
        board[(column, row)] = player   #fix
        return(True)
    else:
        return(False)

def get_piece(board, column, row):
    if not is_free(board, column, row):
        return(board[(column, row)])
    else:
        return(False)

def remove_piece(board, column, row):       #fix
    if not is_free(board, column, row):
        board.pop((column, row))
        return(True)
    else:
        return(False)

def move_piece(board, column, row, newColumn, newRow):
    if not is_free(board, column, row) and is_free(board, newColumn, newRow):
        board[(newColumn, newRow)] = board[(column, row)]
        remove_piece(board, column, row)
        return(True)
    else:
        return(False)

def count(board, axis, axisNumber, player):     #inverterad rad/kolumn i instruktion?
    numberOfPieces = 0
    if axis == "column":
        axisIndex = 0
    elif axis == "row":
        axisIndex = 1

    for piece in board:
        if piece[axisIndex] == axisNumber and get_piece(board,piece[0], piece[1]) == player: 
           numberOfPieces += 1
    return(numberOfPieces)

def nearest_piece(board, column, row):
    if not board:           #check if board is empty
        return(False)
    
    lowestSqrDist = 999999999999

    for piece in board:
        dx = piece[0] - column
        dy = piece[1] - row
        sqrDist = dx*dx + dy*dy
        if sqrDist < lowestSqrDist:
            lowestSqrDist = sqrDist
            nearestPiece = piece
    return(nearestPiece)

