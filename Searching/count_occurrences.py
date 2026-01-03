def count_occurrences(arr, target):
    def first(arr, target):
        low, high = 0, len(arr) - 1
        res = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                res = mid
                high = mid - 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return res

    def last(arr, target):
        low, high = 0, len(arr) - 1
        res = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                res = mid
                low = mid + 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return res

    return last(arr, target) - first(arr, target) + 1

arr = [10, 20, 20, 20, 30]
print(count_occurrences(arr, 20))
