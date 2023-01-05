def nombres_premiers():
    for nombres_premiers in range(2, 1000 + 1):
        if nombres_premiers > 1:
            for i in range(2, nombres_premiers):
                if (nombres_premiers % i) == 0:
                    break
            else:
                print(nombres_premiers)


nombres_premiers()
