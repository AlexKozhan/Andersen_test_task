"""
Дана скобочная последовательность: [((())()(())]]
Можно ли считать эту последовательность правильной?
Если ответ на предыдущий вопрос “нет”, то что необходимо
в ней изменить, чтобы она стала правильной?
"""


def is_valid_bracket_sequence(sequence):
    """
    Check if the given bracket sequence is valid.
    """
    stack = []
    matching_bracket = {')': '(', ']': '['}

    for char in sequence:
        if char in '([':
            stack.append(char)
        elif char in ')]':
            if stack and stack[-1] == matching_bracket[char]:
                stack.pop()
            else:
                return False

    return len(stack) == 0


def fix_bracket_sequence(sequence):
    """
    Fix an unbalanced bracket sequence by adding necessary brackets.
    """
    round_stack = []
    square_stack = []
    result = []

    for char in sequence:
        if char == '[':
            square_stack.append(char)
            result.append(char)
        elif char == ']':
            if square_stack:
                square_stack.pop()
            else:
                result.append('[')
            result.append(char)
        elif char == '(':
            round_stack.append(char)
            result.append(char)
        elif char == ')':
            if round_stack:
                round_stack.pop()
            else:
                result.append('(')
            result.append(char)

    while round_stack:
        result.append(')')
        round_stack.pop()
    while square_stack:
        result.append(']')
        square_stack.pop()

    return ''.join(result)


sequence = "[((())()(())]]"

if is_valid_bracket_sequence(sequence):
    print("The sequence is already valid.")
else:
    print(f"The original bracket sequence: {sequence} is incorrect.")
    # Fix the sequence
    fixed_sequence = fix_bracket_sequence(sequence)
    print("The fixed sequence is:", fixed_sequence)
