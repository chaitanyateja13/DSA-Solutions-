arr = [1, 4, 6, 8, 9]
target = 10
seen = set()

for num in arr:
    if target - num in seen:
        print("Pair exists:", (num, target - num))
        break
    seen.add(num)
