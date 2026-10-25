class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap=[]
        for num in nums:#n times
            heapq.heappush(min_heap,num)
            if len(min_heap)>k:#heap size is fixed to k
                heapq.heappop(min_heap)#pop ya push like operations cost logk in binary heap
        return min_heap[0]
        #total time complexity is O(N(log(K)))
        #space complexxity is O(K)