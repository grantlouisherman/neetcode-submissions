class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        queue while queue len<k append
        then once we hit that we keep getting max of queue
        popleft and appending and getting the window

        '''
        from collections import deque
        q = deque()
        maxs = []
        for i in nums:
            q.append(i)
            if len(q) >= k:
                maxs.append(max(q))
                q.popleft()
        return maxs