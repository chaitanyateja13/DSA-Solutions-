s = "hello"
stack = []

for ch in s:
    stack.append(ch)

reversed_str = ""
while stack:
    reversed_str += stack.pop()

print(reversed_str)
