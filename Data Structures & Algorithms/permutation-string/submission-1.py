class Solution:
    def create_freq_table(self, s:str):
        freq_table = {}
        item_amount = 0
        for i in s:
            if i not in freq_table:
                freq_table[i] = 0
            item_amount+=1
            freq_table[i]+=1
        return (freq_table, item_amount)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        b_table, l = self.create_freq_table(s1)
        curr_table = {}
        window_start = 0
        counter = 0
        for window_end in range(len(s2)):
            i = s2[window_end]
            if i not in curr_table:
                curr_table[i] = 0
            curr_table[i] +=1
            counter +=1
            if counter == l:
                if b_table == curr_table:
                    return True
                t = s2[window_start]
                curr_table[t] -= 1
                if curr_table[t] == 0:
                    del curr_table[t]
                window_start+=1
                
                counter-=1
        return b_table == curr_table
        