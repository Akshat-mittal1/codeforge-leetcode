class Solution(object):
    def maxSubsequence(self, nums, k):
        n = len(nums)
        vals = [[i, nums[i]] for i in range(n)]  # auxiliary array
        vals.sort(key=lambda x: -x[1])           # sort by value descending
        vals = sorted(vals[:k])                  # pick k and sort by index
        res = [val for idx, val in vals]         # extract values
        return res


# Test Case
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubsequence([2, 1, 3, 3], 2))  # Output: [3, 3]
