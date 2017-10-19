"""

A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps.

Write a function:

    def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5.

Assume that:

        N is an integer within the range [1..2,147,483,647].

Complexity:

        expected worst-case time complexity is O(log(N));
        expected worst-case space complexity is O(1).

"""


def integer_to_binary(n):
    if n == 1:
        return str(1)
    else:
        return integer_to_binary(n/2) + str(n % 2)

def solution(N):
    flag = False
    list_count = []
    count = 0
    # print integer_to_binary(N)
    for i in integer_to_binary(N):
        if flag and i == '0':
            count += 1
        elif i == '1' and (not flag):
            flag = True
        elif i == '1' and flag:
            # flag = False
            list_count.append(count)
            count = 0
    # print list_count
    return 0 if list_count == [] else max(list_count)



print solution(2147483647)
print solution(20)
print solution(529)
print solution(328)
print solution(1162)
