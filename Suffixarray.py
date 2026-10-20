nums = [3, 1, 5, 2, 4]

n = len(nums)
suff_min = [0] * n

suff_min[n - 1] = nums[n - 1]

for i in range(n - 2, -1, -1):
    suff_min[i] = min(nums[i], suff_min[i + 1])

print(suff_min)
suff_max= [0] * n

suff_max[n - 1] = nums[n - 1]

for i in range(n - 2, -1, -1):
    suff_max[i] = max(nums[i], suff_max[i + 1])

print(suff_max)
suff_sum= [0] * n

suff_sum[n - 1] = nums[n - 1]

for i in range(n - 2, -1, -1):
    suff_sum[i] = nums[i] + suff_sum[i + 1]

print(suff_sum)