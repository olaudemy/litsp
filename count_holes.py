def count_holes(n):
    counter = 0
    norm = str(n).lstrip('-0 ')
    if not norm.isdigit():
        return "ERROR"
    for i in norm:
                if i in '4690':
                    counter += 1
                elif i == '8':
                    counter += 2
    return counter
