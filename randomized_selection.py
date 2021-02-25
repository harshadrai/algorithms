import numpy as np

def randomized_selection(X,ith_smallest):
    if ith_smallest>len(X)-1:
        return "Length of Array is smaller than "+str(ith_smallest)
    if len(X)==1:
        return X[0]
    else:
        pivot_element_index=np.random.random_integers(0,len(X)-1)
        pivot_element=X[pivot_element_index]
        X[0],X[pivot_element_index]=pivot_element,X[0]
        i=0
        for j in range(1,len(X)):
            if X[j]<pivot_element:
                X[i+1],X[j]=X[j],X[i+1]
                i+=1
        X[0],X[i]=X[i],X[0]
        print(i,X,pivot_element)
        if i==ith_smallest:
            return X[i]
        elif i>ith_smallest:
            return randomized_selection(X[:i],ith_smallest)
        else:
            return randomized_selection(X[i+1:],ith_smallest-i-1)

randomized_selection([2,3,1,6,4,8,7,9,5],8) #ith smallest starts from 0. so replacing 8 with 0 would give 1 as the output
