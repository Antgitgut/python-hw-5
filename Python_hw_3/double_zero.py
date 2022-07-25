def double_zero(array):

    L = array

    for i in L:
        if L[i] == 0:
            L.insert(i, 0)


            print(L)

double_zero([1, 2, 3, 4, 5, 0, 3, 0])

