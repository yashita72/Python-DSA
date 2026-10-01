class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        depth=0
        answer=[]
        for char in seq:
            if char=="(":
                depth+=1
                if depth%2==0:
                    group=1
                    answer.append(group)
                else:
                    group=0
                    answer.append(group)
            if char==")":
                if depth%2==0:
                    group=1
                    answer.append(group)
                else:
                    group=0
                    answer.append(group)
                depth-=1
        return answer
            


        