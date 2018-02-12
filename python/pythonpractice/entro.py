from math import log

def entropy_set(setps):
    summ = sum(setps)
    entp = 0
    for s in setps:
        p = (s/float(summ))
        entp += -(p)*log(p,2)
    return entp
