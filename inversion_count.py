def merge_sort_and_count(X):
    if len(X)==1:
        return(X,0)
    else:
        C=[]
        A,first_half_count=merge_sort_and_count(X[:len(X)//2])
        B,second_half_count=merge_sort_and_count(X[len(X)//2:])
        merge_count=0
        for i in range(len(X)):
            if not B:
                C.extend(A)
                break
            elif not A:
                C.extend(B)
                break
            elif A[0]>B[0]:
                merge_count+=len(A)
                C.append(B[0])
                B=B[1:]
            else:
                C.append(A[0])
                A=A[1:]
        final_count=first_half_count+second_half_count+merge_count
        return(C,final_count)

def inversion_count(X):
    sorted_array,count=merge_sort_and_count(X)
    return count

my_array=[1,3,5,2,4,6]
inversion_count(my_array)
