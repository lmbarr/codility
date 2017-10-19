def two_char_valid(T):
    characT = list(filter(lambda x: x != ':', T))
    list_num = [int(c) for c in T.split(':')]
    return True if len(set(characT)) == 1 or len(set(characT)) == 2 else False

def get_time(begin_t):
    while True:
        #print "get", begin_t
        if two_char_valid(begin_t):
            #print begin_t
            yield begin_t
        list_num = [int(c) for c in begin_t.split(':')]
        list_num1 = list(list_num)
        if list_num[2] < 59:
            list_num[2] += 1
        else:
            if list_num[1] < 59:
                list_num[1] += 1
                list_num[2] = 0
            else:
                if list_num[0] < 23:
                    list_num[0] += 1
                    list_num[1] = 0
                    list_num[2] = 0
                else:
                    list_num = [0, 0, 0]
        begin_t = reduce(lambda x,y: x +':'+ y, ['{:02d}'.format(x) for x in list_num])

# def solution(S, T):
#     gen = get_time(S)
#     def f_rec(val):
#         val = next(gen)
#         if lower_than(val, T) or  (lower_than(S, val) or equal(S, val)):
#             return []
#         else:
#             return f_rec(val) + [val]
#
#     fst = next(gen)
#     lista_final = f_rec(S)
#     lista_final.append(fst)
#     return lista_final

def lower_than(S, T):
    list_num1 = [int(c) for c in S.split(':')]
    list_num2 = [int(c) for c in T.split(':')]
    bigger = map(lambda x, y: x > y, list_num1, list_num2)
    lower = map(lambda x, y: x < y, list_num1, list_num2)
    equal = map(lambda x, y: x == y, list_num1, list_num2)

    for i in range(len(bigger)):
        if bigger[i]:
            return True
            break
        elif lower[i]:
            return False
            break
        elif equal[i] and i==(len(bigger)-1):
            return False

def equal(S, T):
    list_num1 = [int(c) for c in S.split(':')]
    list_num2 = [int(c) for c in T.split(':')]
    aux = map(lambda x,y: x == y, list_num1, list_num2)
    return reduce(lambda x,y: x and y, aux)

def solution(S, T):
    gen = get_time(S)
    lista = []
    val = next(gen)
    if (lower_than(val, S) or equal(val, S)) and (equal(T, val) or lower_than(T, val)):
        lista.append(val)
    val = next(gen)
    while (lower_than(T, val) or equal(val, T)) and lower_than(val, S):
        # print val, T
        lista.append(val)
        #print S, val, T,lower_than(T, val)
        val = next(gen)
    print lista
    return len(lista)

print solution('00:00:00', '23:59:59')
print solution('15:15:00','15:15:12')
print solution('22:22:21','22:22:23')
print solution('23:23:21','23:23:22')
print solution('23:45:38','23:45:39')
print solution('00:11:00','00:11:01')
print solution('22:00:00', '23:32:32')
print solution('00:00:23', '00:00:24')
