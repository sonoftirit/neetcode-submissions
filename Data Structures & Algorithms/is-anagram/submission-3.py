class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        table1 = {} #key value pair of chracter and count
        table2 = {}

        for c in s:
            table1[c] = table1.get(c, 0) + 1 

        for c in t:
            table2[c] = table2.get(c, 0) + 1
        
        return table1 == table2


        