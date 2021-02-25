import math


def merge_sort(X, list_of_indices=[]):
    if not list_of_indices:
            list_of_indices=list(range(len(X)))
    if len(X)==1:
        return(X,list_of_indices)
    else:
        A,A_list_of_indices=merge_sort(X[:len(X)//2], list_of_indices[:len(X)//2])
        B,B_list_of_indices=merge_sort(X[len(X)//2:], list_of_indices[len(X)//2:])
        C=[]
        final_list_of_indices=[]
        for i in range(len(X)):
            if not A:
                C.extend(B)
                final_list_of_indices.extend(B_list_of_indices)
                break
            elif not B:
                C.extend(A)
                final_list_of_indices.extend(A_list_of_indices)
                break
            elif A[0]<B[0]:
                C.append(A[0])
                final_list_of_indices.append(A_list_of_indices[0])
                A=A[1:]
                A_list_of_indices=A_list_of_indices[1:]
            else:
                C.append(B[0])
                final_list_of_indices.append(B_list_of_indices[0])
                B=B[1:]
                B_list_of_indices=B_list_of_indices[1:]
        return(C,final_list_of_indices)

def euclidean_distance(A, B):
    return math.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)


def closest_pairs(A):
    if len(A)==1:
        return(math.inf,A[0],None)
    elif  len(A)==2:
        return(euclidean_distance(A[0],A[1]),A[0],A[1])
    else:
        A_sorted_X_coordinates,A_indices_sorted_by_X_coordinates=merge_sort([i[0] for i in A])
        A_sorted_Y_coordinates,A_indices_sorted_by_Y_coordinates=merge_sort([i[1] for i in A])
        A_sorted_by_X_coordinates=list(map(A.__getitem__,A_indices_sorted_by_X_coordinates))
        d_left,A1_left,A2_left=closest_pairs(A_sorted_by_X_coordinates[:(len(A)//2)+1])
        d_right,A1_right,A2_right=closest_pairs(A_sorted_by_X_coordinates[(len(A)//2)+1:])
        if d_left<d_right:
            d_min=d_left
            A1_best_contender=A1_left
            A2_best_contender=A2_left
        else:
            d_min=d_right
            A1_best_contender=A1_right
            A2_best_contender=A2_right
        mid_point=A_sorted_by_X_coordinates[len(A)//2]
        left_split_points_in_d_min=[i for i in A_sorted_by_X_coordinates[:(len(A)//2)+1] if i[0]>mid_point[0]-d_min]
        right_split_points_in_d_min=[i for i in A_sorted_by_X_coordinates[(len(A)//2)+1:] if i[0]<mid_point[0]+d_min]
        for i in left_split_points_in_d_min:
            right_side_candidates=[j for j in right_split_points_in_d_min if j[1]<i[1]+d_min and j[1]>i[1]-d_min]
            for j in right_side_candidates:
                distance=euclidean_distance(i,j)
                if d_min>distance:
                    d_min=distance
                    A1_best_contender=i
                    A2_best_contender=j
        return(d_min,A1_best_contender,A2_best_contender)


A= [[2, 3], [12, 30], [40, 50], [5, 1], [12, 10], [3, 4]]
closest_pairs(A) #The smallest distance is 1.414214
