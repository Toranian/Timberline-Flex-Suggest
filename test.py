def suggest_amount(ls, amount):
    out = []
    for i in range(amount):
        highest = max(ls)
        out.append(highest)
        ls.remove(highest)
    return out

def highest(ls):
    out = []

    for i in range(3):
        highest = max(ls)
        print(highest)
        out.append(highest)
        print("out", out)
        ls.remove(highest)

suggest_amount([1, 2, 5, 7], 2)
#
# highest([1, 5, 6, 9])
