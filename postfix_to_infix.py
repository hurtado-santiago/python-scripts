def infix(postfix):
    """Convert postfix to infix, using the fewest parentheses needed.

    Returns "invalid" (or "format invalid") if the input isn't a valid
    postfix expression.
    """
    weight = {"+": 0, "-": 0, "*": 1, "/": 1}
    pile = []

    for char in postfix:
        if char == " ":
            continue
        elif char in weight.keys():
            if len(pile) < 2:
                return "format invalid"
            aux2 = pile.pop()
            aux1 = pile.pop()
            if len(aux2) > 1 and ((weight[aux2[1]] <= weight[char])):
                aux2 = f"({aux2[0]})"
            else:
                aux2 = aux2[0]

            if len(aux1) > 1 and weight[aux1[1]] < weight[char]:
                aux1 = f"({aux1[0]})"
            else:
                aux1 = aux1[0]

            pile.append([f"{aux1}{char}{aux2}", char])

        elif (char >= "a" and char <= "z") or (char >= "A" and char <= "Z"):
            pile.append([char])
        else:
            return "format invalid"
    if len(pile) != 1:
        return "invalid"
    return pile.pop()[0]


# tests = ['ab+c*', 'abc*+', 'abc/+*', 'ab+c d-*', 'abc/+', 'a', 'd*', '+-', '/p', 'ab^c d-', 'abc++']
tests = ["abc**"]


for x in tests:
    result = infix(x)
    print(f"{x:10} ==> {result}")
