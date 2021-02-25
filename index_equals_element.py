def index_equals_element(X, index_list=[]):
    if not index_list:
        index_list=list(range(len(X)))
    if len(X)==1:
        if X[0]==index_list[0]:
            return True
        else:
            return False
    else:
        center_element=X[len(X)//2]
        if center_element==index_list[len(X)//2]:
            return True
        elif center_element<index_list[len(X)//2]:
            return index_equals_element(X[len(X)//2+1:],index_list[len(X)//2+1:])
        else:
            return index_equals_element(X[:len(X)//2],index_list[:len(X)//2])

index_equals_element([-7,-5,-3,-2,0,1,3,5,6,7,8,10,12,15,17]) #Should be True
index_equals_element([-7,-5,-3,-2,0,1,3,5,6,7,8,10,13,15,17]) #Should be False
index_equals_element([0]) #Should be True
index_equals_element([-5,-4,-3,-2,-1,5]) #Should be True