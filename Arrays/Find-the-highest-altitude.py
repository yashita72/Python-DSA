class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        prefix_sum=[0]*(len(gain)+1)
        prefix_sum[0]=0
        prefix_sum[1]=gain[0]
        for i in range(1,len(gain)):
            prefix_sum[i+1] = prefix_sum[i]+gain[i]
        maxx= prefix_sum[0]
        for i in range(len(prefix_sum)):
            maxx=max(maxx,prefix_sum[i])
        return maxx
        

    

 
        