class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        loop through a check everything n*m
        sort every item and then just group
        I can create scores of each word and then try to find complement
        '''
        t = {}
        for s in strs:
            score = "".join(sorted(s))
            if score not in t:
                t[score] = []
            t[score].append(s)
        
        return list(t.values())