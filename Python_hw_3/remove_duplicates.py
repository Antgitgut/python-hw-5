def remove_duplicates(array):
    L = array

    L2 = [i for n, i in enumerate(L) if i not in L[:n]]
    print(L2)


remove_duplicates([1, 1, 3, 3, 5, 5, 5, 5])
