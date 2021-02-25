import numpy

def quick_sort(X):
    if not X:
        return []
    elif len(X)==1:
        return X
    else:
        pivot_element_index=numpy.random.random_integers(0,len(X)-1)
        pivot_element=X[pivot_element_index]
        X[0],X[pivot_element_index]=pivot_element,X[0]
        i=0
        for j in range(1,len(X)):
            if X[j]<pivot_element:
                X[i+1],X[j]=X[j],X[i+1]
                i+=1
        X[0],X[i]=X[i],X[0]
        X[:i]=quick_sort(X[:i])
        X[i+1:]=quick_sort(X[i+1:])
        return X

quick_sort([2,5,3,7,4,8,1,9,6])
quick_sort([2,5,3,7,4,-3,-9,8,1,9,0,6])
quick_sort([2])
quick_sort([])

################## For Number of Comparisons: Below code ###########################
# import numpy
# import math
# import statistics

# def quick_sort(X,number_of_comparisons=0):
#     if not X:
#         return([],0)
#     elif len(X)==1:
#         return(X,0)
#     else:
#         pivot_element_index=numpy.random.random_integers(0,len(X)-1)
#         pivot_element=X[pivot_element_index]
#         X[0],X[pivot_element_index]=pivot_element,X[0]
#         i=0
#         for j in range(1,len(X)):
#             if X[j]<pivot_element:
#                 X[i+1],X[j]=X[j],X[i+1]
#                 i+=1
#         X[0],X[i]=X[i],X[0]
#         X[:i],left_number_of_comparisons=quick_sort(X[:i],number_of_comparisons)
#         X[i+1:],right_number_of_comparisons=quick_sort(X[i+1:],number_of_comparisons)
#         number_of_comparisons+=len(X)-1
#         number_of_comparisons+=left_number_of_comparisons+right_number_of_comparisons
#         return(X,number_of_comparisons)