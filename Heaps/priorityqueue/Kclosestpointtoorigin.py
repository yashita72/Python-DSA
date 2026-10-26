from cmath import sqrt
import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        max_heap=[]#we need the minimum distance points#to sabse bda distance top pr ana chahie thats why we did -distance bcs python ka in built heapq do the min heap operation which means ki sabse chota top pr ayega 
        for x,y in points:#len(points)
          dist=-(sqrt(x*x+y*y))
          heapq.heappush(max_heap,(dist,x,y))
          if len(max_heap)>k:#Nlogk
            heapq.heappop(max_heap)
        return [[x,y] for (dist,x,y) in max_heap]
        #total time complexity is O(Nlog(K))
        #space complexity is O(K)
        
     