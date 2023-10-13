def twoSum(nums: list[int], target: int) -> list[int]:
    _map = dict()
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in _map:
            return [_map[comp], i]
        else:
            _map[nums[i]] = i

    return [-1, -1]


def twoNumberSum(array, targetSum):
    _map = dict()
    ret = []
    for i in array:
        breakpoint()
        diff = targetSum - i
        if diff in _map and diff is not i:
            return [i, diff]
        else:
            _map[diff] = 1

    return ret


# print(twoNumberSum([3, 11, -4, -1], 10))

# print(twoSum([2, 7, 11, 15], 9))
# print(twoSum([3, 2, 4], 6))
# print(twoSum([3, 3], 6))
