# Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

def solution(a):
    l = sorted([i for i in a if i > 0])
    for n,i in enumerate(a):
        if i == -1:
            l.insert(n,i)
    return l