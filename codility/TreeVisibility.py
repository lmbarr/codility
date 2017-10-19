class Node:
    def __init__(self, val, n1, n2):
        self.l = n1
        self.r = n2
        self.x = val

def solution(T):
    def f_rec(n, max_value):
        if n == None:
            return 0
        else:
            if n.x >= max_value:
                return 1 + f_rec(n.l, n.x) + f_rec(n.r, n.x)
            else:
                return f_rec(n.l, max_value) + f_rec(n.r, max_value)
    return f_rec(T, 0 if T == None else T.x)

T = Node(800000, Node(2, Node(8000000, None, None), Node(7000000, None, None)), Node(6, None, None))
T2 = Node(5, Node(3, Node(20, None, None), Node(21, None, None)), Node(10, Node(1, None, None), None))
T5 = Node(11, Node(3, Node(20, None, None), Node(21, None, None)), Node(10, Node(1, None, None), None))
T6 = Node(8, Node(2, Node(8, None, None), Node(7, None, None)), Node(6, None, None))
T3 = None
T4 = Node(1, None, None)
T7 = Node(8**100, Node(2, Node(8, None, None), Node(7, None, None)), Node(6, None, None))
T8 = Node(5, Node(50, Node(20, None, None), Node(21, None, None)), Node(10, Node(1, None, None), None))
T9 = Node(3, Node(12, None, None), None)
T10 = Node(1, Node(3, Node(12, Node(10, Node(3, None, None), None), None), None), Node(4, None, None))
T8.r = T10
Tbig = Node(1, Node(1, Node(3, Node(30,T8, T10), T2), T8), Node(1, Node(3, Node(30,T8, T10), T2), T8))
Tbigger = Node(10**100, Node(100, Tbig, Tbig), Tbig)

T = Node(1, Node(1, Node(1, Tbigger, Tbigger), Node(1, Tbigger, Tbigger)), Node(1, Node(1, Tbigger, Tbigger), Node(1, Tbigger, Tbigger)))
Tg = Node(0, Node(0, Node(0, T, T), Node(0, T, T)), Node(0, Node(0, T, T), Node(0, T, T)))

print solution(T2) == 4
print solution(T3) == 0
print solution(T4) == 1
print solution(T6) == 2
print solution(T5) == 3
print solution(T7) == 1
print solution(T8) == 3
print solution(T9) == 2
print solution(T10) == 4
print solution(T8) == 3
print solution(Tbig)
print solution(Tg)
