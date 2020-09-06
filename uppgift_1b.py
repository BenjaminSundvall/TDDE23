def max2(x, y):
    if x >= y:
        return(x)
    else: 
        return(y)

def max3(x, y, z):
    return(max2(x, max2(y, z)))
