def bubbles(n, n_rev):
    # define the number of comparings in n. This allows to escape the error of comparings of last element with no element. 
    number_of_comp = len(n) -1
    # Each element should be compared
    for i in range(number_of_comp):
        # take element j from the n and compare to element j+1
        for j in range(number_of_comp - i):
            if n[j] > n[j+1]:
                # if first element is greater, it becomes the second element
                n[j], n[j+1] = n[j+1], n[j]
    #reversed sorting
    n_rev = n[::-1]
    return n, n_rev
