# You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

def solution(inputArray):
    moves = 0
    for i in range(1, len(inputArray)):
        current, prev = inputArray[i], inputArray[i-1]
        if current<=prev:
            moves += prev + 1 - current
            inputArray[i] = prev + 1
        
    return moves