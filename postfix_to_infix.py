# Operators where swapping evaluation order changes the result, so a
# same-precedence right operand still needs parentheses.
NON_ASSOCIATIVE = "-/"

PRECEDENCE: dict[str, int] = {"+": 0, "-": 0, "*": 1, "/": 1}


def infix(postfix: str) -> str:
    """Convert postfix to infix, using the fewest parentheses needed.

    Returns "invalid" (or "format invalid") if the input isn't a valid
    postfix expression.
    """
    stack: list[list[str]] = []

    for char in postfix:
        if char == " ":
            continue
        elif char in PRECEDENCE:
            if len(stack) < 2:
                return "format invalid"
            right = stack.pop()
            left = stack.pop()
            if len(right) > 1 and (
                PRECEDENCE[right[1]] < PRECEDENCE[char]
                or (PRECEDENCE[right[1]] == PRECEDENCE[char] and char in NON_ASSOCIATIVE)
            ):
                right = f"({right[0]})"
            else:
                right = right[0]

            if len(left) > 1 and PRECEDENCE[left[1]] < PRECEDENCE[char]:
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


if __name__ == "__main__":
    # tests = ['ab+c*', 'abc*+', 'abc/+*', 'ab+c d-*', 'abc/+', 'a', 'd*', '+-', '/p', 'ab^c d-', 'abc++']
    tests = ["abc**"]

    for expr in tests:
        result = infix(expr)
        print(f"{expr:10} ==> {result}")
