import math 
def score(x, y):
    lands = math.sqrt(x*x+y*y)
    
    if lands <= 1:
        return 10
    elif lands <= 5:
        return 5
    elif lands <= 10:
        return 1
    else:
        return 0
    
        