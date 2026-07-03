def three_sum(arr):
    arr.sort()
    n = len(arr)
    result = []
  #time complexity is big oh of n square while brute force ki n cube hoti and sorting algo used is timsort uski complexxity is big oh of n log n space ccomplexity is bg oh of n
  
    for fix in range(n):
        # skip duplicate fixed numbers
        if fix > 0 and arr[fix] == arr[fix - 1]:
            continue

        # early exit optimizations
        if arr[fix] > 0:
            break  # smallest number is positive, sum can't be 0

        left, right = fix + 1, n - 1
        target = -arr[fix]

        while left < right:
            curr_sum = arr[left] + arr[right]

            if curr_sum == target:
                result.append([arr[fix], arr[left], arr[right]])
                left += 1
                right -= 1
                # skip duplicates for left
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                # skip duplicates for right
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1
            elif curr_sum < target:
                left += 1
            else:
                right -= 1

    return result