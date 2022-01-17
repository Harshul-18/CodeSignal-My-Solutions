# Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

def solution(year):
    centuary = year - year%100
    if year == centuary:
        return int(str(centuary)[:-2])
    else:
        return int(str(centuary+100)[:-2])
