def bubbles(n, n_rev):
    # define the number of compearings in n. This allows to escape the error of comparings of last element with no element. 
    numberOfComp = len(n) -1
    # Each element should be compeared
    for i in range(numberOfComp):
        # take element j from the n and compare to element j+1
        for j in range(numberOfComp - i):
            if n[j] > n[j+1]:
                # if first element is greater, it becomes the second element
                n[j], n[j+1] = n[j+1], n[j]
    #reversed sorting
    n_rev = n[::-1]
    return n, n_ver
