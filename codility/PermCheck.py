def solution(A):
    A.sort()
    if len(A) == 1 and A[0] != 1:
        return 0
    else:
        if range(1, len(A) + 1) == A:
            return 1
        else:
            return 0

        # for i in range(1, len(A) + 1):
        #     if i == A[i-1]:
        #         continue
        #     else:
        #         return 0
        # return 1

print solution([4, 1, 3, 2])
print solution([1])
print solution([2])
print solution([1, 1, 2])
print solution([20**1000])
print solution([4, 3, 2])
print solution(list(set(range(1,100000))- set([10])))
