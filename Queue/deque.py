from collections import deque

dq = deque()

dq.append(10)      # add rear
dq.appendleft(20)  # add front

print(dq)

dq.pop()           # remove rear
dq.popleft()       # remove front

print(dq)
