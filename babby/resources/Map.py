#Map module
#Andrew M. Blasius

from llist import sllist
from math import abs

def search(map,position,tol):
    '''Searches for an x-position in the linked list'''
    while True:
        entry = map.popleft()
        if abs(entry[0] - position) < tol:
            return entry   

def initMap():
    map = sllist()
    return map


