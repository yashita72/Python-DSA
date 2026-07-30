class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        integer=0
        i=0
        while(i<len(s)):
            if s[i]=='M':
                integer+=1000
                i+=1
            elif i+1 < len(s) and s[i]=='C' and s[i+1] == 'M':
                integer+=900
                i+=2
            elif i+1 < len(s) and s[i]=='C' and s[i+1] == 'D':
                integer+=400
                i+=2
            elif i+1 < len(s) and s[i]=='X' and s[i+1] == 'C':
                integer+=90
                i+=2
            elif i+1 < len(s) and s[i]=='X' and s[i+1] == 'L':
                integer+=40
                i+=2
            elif i+1 < len(s) and s[i]=='I' and s[i+1] == 'X':
                integer+=9
                i+=2
            elif i+1 < len(s) and s[i]=='I' and s[i+1] == 'V':
                integer+=4
                i+=2
            elif s[i]=='D':
                integer+=500
                i+=1
            elif s[i]=='C':
                integer+=100
                i+=1
            elif s[i]=='L':
                integer+=50
                i+=1
            elif s[i]=='X':
                integer+=10
                i+=1
            elif s[i]=='V':
                integer+=5
                i+=1
            elif s[i]=='I':
                integer+=1
                i+=1

        return integer