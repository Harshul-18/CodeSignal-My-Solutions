# Given two cells on the standard chess board, determine whether they have the same color or not.

def cellColor(cell):
    col = ord(cell[0])
    row = int(cell[1])
    if col%2 == row%2:
        return 'dark'
    return 'light'

def solution(cell1, cell2):
    return cellColor(cell1) == cellColor(cell2)