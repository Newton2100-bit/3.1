def pair_div(Lnum, Ldenom):
    assert len(Lnum)  == len(Ldenom),'length diffrence in the inputs'
    if 0 in Ldenom:
        # raise ValueError("You can't divide by zero kindly")
        return [0]

    L = [Lnum[i] / Ldenom[i] for i in range(len(Lnum))]
    return L

l1 = [9, 16, 25]
l2 = [3, 4, 5]
combined = pair_div(l1, l2)
print(combined)

l1 = [9, 16, 25]
l2 = [3, 0, 5]
combined = pair_div(l1, l2)
print(combined)

l1 = [9, 16, 25]
l2 = [3, 4]
combined = pair_div(l1, l2)
print(combined)
