#Take a list of integers and a target sum as input and return a list of unique tuples where each tuple contains tow int from the unput list that sums up to the target

def find_pairs(nums, target):
    pairs = []
    seen = set()

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in seen and (complement, nums[i]) not in pairs:
            pairs.append((nums[i], complement))
        seen.add(nums[i])

    return pairs

nums = [1, 2, 3, 4, 5]
target = 7
pairs = find_pairs(nums, target)
print(pairs)