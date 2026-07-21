class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        dic={}
        for char in s:
            if char in dic:
                  dic[char] += 1
            else:
                 dic[char] = 1
        for char in t:
            if char in dic:
                  dic[char] -= 1
            else:
                 dic[char] = -1
        for count in dic.values():
            if count != 0:
                return False
        return True
    # dic[char] = dic.get(char, 0) + 1