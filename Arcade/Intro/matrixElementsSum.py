# Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, your task is to return the total sum of all rooms that are suitable for the CodeBots (ie: add up all the values that don't appear below a 0).

def solution(matrix):
    result = 0
    below0 = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            current = matrix[i][j]
            if current == 0:
                below0.append(j)
            if j in below0:
                continue
            else:
                result += current
    return result