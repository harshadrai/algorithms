def find_largest_unimodal_element(X):
    if len(X)==1:
        return X[0]
    else:
        left_half=X[:len(X)//2]
        right_half=X[len(X)//2:]
        if left_half[-1]>right_half[0]:
            return find_largest_unimodal_element(left_half)
        else:
            return find_largest_unimodal_element(right_half)

find_largest_unimodal_element([1,2,4,5,7,9,6,3,2,1])