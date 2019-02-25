'''
Created on 10 Aug 2018

@author: benos
'''
from mpmath import mpmathify, mpf


def logHistogramAdd(start, end, size, dist, value):
    start = mpf(start)
    end = mpf(end)
    step = mpf((end - start) / size)
    for i in range(1, size):
        current = mpmathify(10 ** (start + step * i))
        if value < current:
            dist[i - 1] += 1
            return dist
    dist[-1] += 1
    return dist


def logHistogramAddMult(start, end, size, dist, value, mult, lastIndex):
    start = mpf(start)
    end = mpf(end)
    step = mpf((end - start) / size)
    for i in range(lastIndex, size):
        current = mpmathify(10 ** (start + step * i))
        if value < current:
            dist[i - 1] += mult
            lastIndex = i
            return (lastIndex, dist)
    dist[-1] += mult
    lastIndex = size
    return (lastIndex, dist)
