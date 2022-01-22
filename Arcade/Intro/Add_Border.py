# Given a rectangular matrix of characters, add a border of asterisks(*) to it.

def solution(picture):
    rows = len(picture[0])+2
    return ["*"*rows] + [f"*{i}*" for i in picture] + ["*"*rows]