from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for x in nums:
            if nums.count(x) == 1:
                return x


s = Solution()
print(s.singleNumber([1, 2, 3, 2, 3, 1, 4]))
