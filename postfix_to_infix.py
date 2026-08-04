def infix(postfix: str) -> str:
    """Convert postfix to infix, using the fewest parentheses needed.

    Returns "invalid" (or "format invalid") if the input isn't a valid
    postfix expression.
    """
    weight: dict[str, int] = {"+": 0, "-": 0, "*": 1, "/": 1}
    stack: list[list[str]] = []

    for char in postfix:
        if char == " ":
            continue
        elif char in weight.keys():
            if len(stack) < 2:
                return "format invalid"
            right = stack.pop()
            left = stack.pop()
            if len(right) > 1 and (
                weight[right[1]] < weight[char]
                or (weight[right[1]] == weight[char] and char in "-/")
            ):
                right = f"({right[0]})"
            else:
                right = right[0]

            if len(left) > 1 and weight[left[1]] < weight[char]:
                left = f"({left[0]})"
            else:
                left = left[0]

            stack.append([f"{left}{char}{right}", char])

        elif char.isalpha():
            stack.append([char])
        else:
            return "format invalid"
    if len(stack) != 1:
        return "invalid"
    return stack.pop()[0]


# tests = ['ab+c*', 'abc*+', 'abc/+*', 'ab+c d-*', 'abc/+', 'a', 'd*', '+-', '/p', 'ab^c d-', 'abc++']
tests = ["abc**"]


for expr in tests:
    result = infix(expr)
    print(f"{expr:10} ==> {result}")
