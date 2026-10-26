import heapq
from collections import Counter #to count frequencies 
from collections import deque#double ended queue used here tostore the cooling period and tasks temeporaly
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count=Counter(tasks)#to count freq of each task and store it
        max_heap=[-cnt for cnt in count.values()]#negative freq are stored in max_heap here as a list
        heapq.heapify(max_heap)#now the list is converted to heap
        time=0
        q=deque()#stores pair of [cnt,idle_time]#waiting area
        while max_heap or q:#run untill both heap and q are emptys
            time+=1
            if max_heap:
                #removing the most freq task
                cnt=heapq.heappop(max_heap)
                cnt+=1#as cnt is negative so the cnt will reduce
                if cnt!=0:# means that the task is not completed
                  q.append([cnt,time+n])
            if q and q[0][1] == time:#we check ki queue mein time jo    task h uska aur available time same h to we execute it
                heapq.heappush(max_heap, q.popleft()[0])
        return time
        #time complexity will be O(N)+O(Nlog(26))
        #as log26 is a constant so total final time complexity will be O(N)
        #space complexity is O(26) bcs at max 26 alphabets can be in heap
        #so again  space complexity is O(1)that is constant




        