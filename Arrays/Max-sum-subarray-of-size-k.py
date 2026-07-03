class Solution:
    def maxSum(self, arr, k):
        n = len(arr)
        
        # sum of first window
        window_sum = 0
        for i in range(k):
            window_sum += arr[i]
        
        max_sum = window_sum
        
        # slide the window
        for j in range(k, n):
            window_sum = window_sum - arr[j - k] + arr[j]
            if window_sum > max_sum:
                max_sum = window_sum
        
        return max_sum
    #time complexity big oh of n
    