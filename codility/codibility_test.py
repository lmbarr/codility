"""This is a demo task.

Write a function:

    def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [-1, -3], the function should return 1.

Assume that:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [-1,000,000..1,000,000].

"""

import random
def solution(A):
    # write your code in Python 2.7
    maximo = max(A)
    if maximo < 0:
        return 1
    else:
        l = [False] * (len(A) + 1)
        for elemet in A:
            if elemet > 0 and elemet <= len(A):
                l[elemet] = True
        print l
        for i in range(1, len(l)):
            if not(l[i]):
                return i
        return maximo + 1

print solution([-12,0,12])
print solution([1,0,2])
print solution([-1, -3])
print solution([1,2,3])
# print solution([100,22,0,1,123])
# lista = range(11)
# random.shuffle(lista)
# print solution(lista)
