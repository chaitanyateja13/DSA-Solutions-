def is_valid(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in "({[":
            stack.append(ch)
        else:
            if not stack or stack.pop() != pairs[ch]:
                return False

    return not stack

print(is_valid("()[]{}"))
print(is_valid("(]"))
