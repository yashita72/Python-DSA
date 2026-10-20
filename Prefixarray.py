nums = [3, 1, 5, 2, 4]

prefix = [0] * len(nums)

prefix[0] = nums[0]

for i in range(1, len(nums)):
    prefix[i] = prefix[i - 1] + nums[i]

print(prefix)
prefix_max= [0] * len(nums)

prefix_max[0] = nums[0]

for i in range(1, len(nums)):
    prefix_max[i] = max(prefix_max[i - 1], nums[i])

print(prefix_max)