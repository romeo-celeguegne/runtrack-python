def Calcule(num1, operator, num2):

    if operator == "+":
        return (num1 + num2)
    elif operator == "-":
        return (num1 - num2)
    elif operator == "*":
        return (num1 * num2)
    elif operator == "/":
        return (num1 / num2)


result = Calcule(6, "*", 6)
print(result)
