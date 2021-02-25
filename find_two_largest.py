def find_two_largest(X):
    if len(X)==2:
        if X[0]<X[1]:
            return X
        else:
            return X[::-1]
    else:
        left_half=find_two_largest(X[:len(X)//2])
        right_half=find_two_largest(X[len(X)//2:])
        sorted_four=[]
        for i in range(4):
            if not left_half:
                sorted_four.extend(right_half)
                break
            elif not right_half:
                sorted_four.extend(left_half)
                break
            elif left_half[0]<right_half[0]:
                sorted_four.append(left_half[0])
                left_half=left_half[1:]
            elif left_half[0]>right_half[0]:
                sorted_four.append(right_half[0])
                right_half=right_half[1:]
        return sorted_four[2:]

find_two_largest([3,1,5,2,7,9,4,10])