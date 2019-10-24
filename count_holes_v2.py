def count_holes(n):
    norm = str(n).lstrip('-0 ')
    if not norm.isdigit():
        return "ERROR"
    d = {'4': 1, '6': 1, '9': 1, '0': 1, '8': 2}
    return sum(d.get(i, 0) for i in norm)
