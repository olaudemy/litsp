def balace_ckecker(data):
    pocket = []
    left_br = ["{", "[", "("]
    right_br = ["}", "]", ")"]
    for i in data:
        if i in left_br:
            pocket.append(right_br[ left_br.index(i) ])
        elif i in right_br:
            if pocket and i == pocket[-1]:
                pocket.pop(-1)
            else:
                print("No balace at check_it")
                return
    if pocket:
	print("No balace at check_it")
    else:
        print("The world has balanced check_it")

