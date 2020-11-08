
def merge(dat,p,q,r,desc = False):
    n1 = q-p+1
    n2 = r-q
    L = []
    for i in range(p,q+1):
        L.append(dat[i])
    R = []
    for i in range(q+1,r+1):
        R.append(dat[i])

    i = 0
    j = 0
    for k in range(p,r+1):
        if desc:
            if i>n1-1:
                if j>n2-1:
                    break
                else:
                    dat[k] = R[j]
                    j+=1
            else:
                if j>n2-1:
                    dat[k] = L[i]
                    i+=1
                else:
                    if R[j]<L[i]:
                        dat[k] = L[i]
                        i+=1
                    else:
                        dat[k] = R[j]
                        j+=1
        else:
            if i>n1-1:
                if j>n2-1:
                    break
                else:
                    dat[k] = R[j]
                    j+=1
            else:
                if j>n2-1:
                    dat[k] = L[i]
                    i+=1
                else:
                    if R[j]>L[i]:
                        dat[k] = L[i]
                        i+=1
                    else:
                        dat[k] = R[j]
                        j+=1
    return dat


def merge_sort(dat,p,r,desc = False):

    if not isinstance(dat,(tuple,list,np.ndarray)):
        return dat
    if p<r:
        q = int((p+r)/2)
        merge_sort(dat,p,q,desc)
        merge_sort(dat,q+1,r,desc)
        return merge(dat,p,q,r,desc)
        

