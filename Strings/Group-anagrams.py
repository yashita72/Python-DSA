class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
       
        dic={}
        for s in strs:
            key = ''.join(sorted(s))
            if key in dic:
                dic[key].append(s)
            else:
                dic[key] = [s]
        
        return list(dic.values())