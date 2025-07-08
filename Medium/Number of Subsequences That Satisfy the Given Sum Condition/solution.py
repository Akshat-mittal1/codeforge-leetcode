from bisect import bisect_right

class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        mod = 10**9 + 7
        n = len(nums)
        
        # Precompute powers of 2
        powers = [1] * n
        for i in range(1, n):
            powers[i] = (powers[i - 1] * 2) % mod

        result = 0

        for i in range(n):
            # Binary search for max j where nums[i] + nums[j] <= target
            remain = target - nums[i]
            j = bisect_right(nums, remain) - 1
            
            if j >= i:
                result = (result + powers[j - i]) % mod

        return result

# Example Test
if __name__ == "__main__":
    sol = Solution()
    print(sol.numSubseq([3, 5, 6, 7], 9))  # Output: 4

