def count_holes(n):
    counter = 0
    if type(n) is float:
        print ("ERROR")
    elif type(n) is int:
        modified = list(str(n))
        print(modified)
        while modified[0] == "0":
            modified.remove('0')
        else:
            one = ['4', '6', '9', '0']
            for i in modified:
                if i == '0':
                    pass
                if i in one:
                    counter += 1
                elif i == '8':
                    counter += 2
                else:
                    pass
            return counter
    elif type(n) is str:
        modified = list(n)
        print(modified)
        if modified[0] == "'":
            modified.remove("'")
        else:
            pass
        while modified[0] == "0":
            modified.remove('0')
        else:
            one = ['4', '6', '9', '0']
            for i in modified:
                if i == '0':
                    pass
                if i in one:
                    counter += 1
                elif i == '8':
                    counter += 2
                else:
                    pass
            return counter
    else:
        print(0)
