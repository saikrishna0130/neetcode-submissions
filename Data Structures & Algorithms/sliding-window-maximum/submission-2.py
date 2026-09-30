from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        output = []

        for i in range(len(nums)):

            # Remove indexes outside the window
            while q and q[0] <= i - k:
                q.popleft()

            # Remove smaller elements
            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            q.append(i)

          
            if i >= k - 1:
                output.append(nums[q[0]])

        return output