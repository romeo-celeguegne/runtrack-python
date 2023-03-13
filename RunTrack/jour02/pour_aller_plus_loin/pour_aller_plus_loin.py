def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("Ceci est un triangle.")
    if a == b and b == c:
        print("Le triangle est équilatéral.")
    elif a == b or b == c or a == c:
        if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
            print("Le triangle est isocèle et rectangle.")
        else:
            print("Le triangle est isocèle.")
    elif a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        print("Le triangle est rectangle.")
    else:
        print("Le triangle est quelconque.")


triangle(9, 9, 3)
