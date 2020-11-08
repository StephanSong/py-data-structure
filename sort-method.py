import numpy as np

def insertion_sort(dat,desc = False):
    """
    This functions support the sorting method - insertion. 

    Parameters
    ----------
    dat : a list, or tuple or numpy array
    desc : optional, specify the order style, ascend or descend

    Returns
    -------
    A sorted list, tuple or numpy array.
    If the type is not correct, the dat will be returned as no changed.

    """
    if not isinstance(dat,(tuple,list,np.ndarray)):
        return dat
    length = len(dat)
    
    for i in range(1,length):
        tmp = dat[i]
        j = i-1
        if desc:
            while j>=0 and dat[j] <tmp:
                dat[j+1] = dat[j]
                j-=1
            dat[j+1] = tmp
        else:
            while j>=0 and dat[j] >tmp:
                dat[j+1] = dat[j]
                j-=1
            dat[j+1] = tmp
    return dat
