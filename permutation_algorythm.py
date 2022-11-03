def permute(idx, elements):
    if idx >= len(elements):
        print(elements)
        return

    permute(idx + 1, elements)

    for i in range(idx + 1, len(elements)):
        elements[idx], elements[i] = elements[i], elements[idx]
        permute(idx + 1, elements)
        elements[idx], elements[i] = elements[i], elements[idx]


elements = [1, 2, 3]
permute(0, elements)
