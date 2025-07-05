class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        res = []
        index = [i for i, val in enumerate(nums) if val == key]
        for i in range(len(nums)):
            for j in index:
                if abs(i - j) <= k:
                    res.append(i)
                    break
        res.sort()
        return res


# 🔁 Test Case
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4, 2, 1, 2]
    key = 2
    k = 1
    print(sol.findKDistantIndices(nums, key, k))  # Output: [0, 1, 2, 3, 4, 5, 6]
