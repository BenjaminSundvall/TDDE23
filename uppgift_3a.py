def new_board():
    return({})

def is_free(board, column, row):
    return(not (column, row) in board)

def place_piece(board, column, row, player):
    if is_free(board, column, row):             # check if the current tile is free
        board[(column, row)] = player           # place piece
        return(True)
    else:
        return(False)

def get_piece(board, column, row):
    if not is_free(board, column, row):         # check if there is a piece on the current tile
        return(board[(column, row)])            # return content of target tile
    else:
        return(False)

def remove_piece(board, column, row):
    if not is_free(board, column, row):         # check if there is a piece on the current tile
        board.pop((column, row))                # remove tile from dictionary
        return(True)
    else:
        return(False)

def move_piece(board, column, row, newColumn, newRow):
    if not is_free(board, column, row) and is_free(board, newColumn, newRow):   # check if there is a piece on the current tile and the target tile is free
        board[(newColumn, newRow)] = board[(column, row)]                       # place new piece on target tile
        remove_piece(board, column, row)                                        # remove old piece
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
        if piece[axisIndex] == axisNumber and get_piece(board,piece[0], piece[1]) == player:    # check if the piece is on the correct row
           numberOfPieces += 1
    return(numberOfPieces)

def nearest_piece(board, column, row):
    if not board:                       # check if board is empty
        return(False)

    lowestSqrDist = 10E99               # set a very high initial lowest distance

    for piece in board:                 # check squared distance between piece and current tile
        dx = piece[0] - column
        dy = piece[1] - row
        sqrDist = dx*dx + dy*dy
        if sqrDist < lowestSqrDist:
            lowestSqrDist = sqrDist
            nearestPiece = piece
    return(nearestPiece)
