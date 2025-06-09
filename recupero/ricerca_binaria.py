def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return True
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


nums = [1, 3, 5, 7, 9, 11]
print(binary_search(nums, 7))
print(binary_search(nums, 2))