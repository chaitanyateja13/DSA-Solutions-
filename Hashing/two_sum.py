nums = [2, 7, 11, 15]
target = 9
hash_map = {}

for i, num in enumerate(nums):
    complement = target - num
    if complement in hash_map:
        print([hash_map[complement], i])
    hash_map[num] = i
