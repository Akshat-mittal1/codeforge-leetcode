class Solution(object):
    def removeElement(self, nums, val):
        l = len(nums)
        c = l - nums.count(val)
        while val in nums:
            nums.remove(val)
        for _ in range(l - c):
            nums.append('_')  # Optional, for visualization
        return c

# ✅ Example usage
if __name__ == "__main__":
    sol = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    k = sol.removeElement(nums, val)
    print("New length:", k)           # Output: 2
    print("Modified nums:", nums)     # Output: [2, 2, '_', '_'].
