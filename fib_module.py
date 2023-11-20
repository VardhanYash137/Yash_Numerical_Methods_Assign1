import numpy as np

def fib_series(n):
    ans_list=np.ones((n))
    ans_list[0]=0
    for i in range(3,n):
        ele=ans_list[i-1]+ans_list[i-2]
        ans_list[i]=ele
    return ans_list

