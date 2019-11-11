import operator

def bubbles(iterable, compare=operator.gt, reverse=False):
    """Function sorts data using bubble sorting algorithm
    Args:
     - iterable
     - compare method
     - reverse (boolean)
    Steps:
     1. Each element in iterable data is compared to next element
     2. Swap in case when one of the conditions is true: 
        - first element is greater then next
        - reverse is false 
    Returns:
     sorted iterable data"""
    
    #make all data iterable
    data = list(iterable)
    # define the number of comparings in n. This allows to escape the error of comparings of last element with no element
    number_of_comp = len(data) -1
    # Each element should be compared
    for i in range(number_of_comp):
        # take element j from the data and compare to element j+1
        for j in range(number_of_comp - i):
            # One of the condition should be true: or first element is greater or the reverse if False
            if operator.xor(compare(data[j], data[j+1]), reverse):
                data[j], data[j+1] = data[j+1], data[j]
    return data
