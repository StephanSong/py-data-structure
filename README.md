# py-data-structure

first sort method - insertion

# use the following codes to test the sorting method

## for the insertion-sort
import numpy as np

dat = np.random.randn(20)

print(dat)
dat = insertion_sort(dat)
print(dat)

## for the merge sort
dat = np.random.randn(20)
dat = merge_sort(dat,0,len(dat)-1)

