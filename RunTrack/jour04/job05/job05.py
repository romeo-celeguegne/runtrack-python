L = [2, 4, 6, 8, 10]
print(L[1])


def somme_cases_voisines():
    result = L[2] + L[4]
    L.insert(3, result)
    print(L[3])
    print(L[-1])


somme_cases_voisines()
