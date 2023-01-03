def calcule(num1, operator, num2):
    if operator == "+":
        print(num1+num2)
    elif operator == "-":
        print(num1-num2)
    elif operator == "*":
        print(num1*num2)
    elif operator == "/":
        print(num1/num2)
    elif operator == "%":
        print(num1 % num2)


calcule(4, "+", 5)
calcule(5, "-", 4)
calcule(4, "*", 5)
calcule(4, "/", 2)
