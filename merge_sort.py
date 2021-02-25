def merge_sort(X):
    if len(X)==1:
        return X
    else:
        C=[]
        half_X_len=len(X)//2
        A=merge_sort(X[:half_X_len])
        B=merge_sort(X[half_X_len:])
        for k in range(len(X)):
            if not A:
                C.extend(B)
                break
            elif not B:
                C.extend(A)
                break
            else:
                if A[0]>B[0]:
                    C.append(B[0])
                    B=B[1:]
                else:
                    C.append(A[0])
                    A=A[1:]
        return C