class Solution:
    def findLHS(self, nums):
        nums.sort()
        j = 0
        maxLength = 0

        for i in range(len(nums)):
            while nums[i] - nums[j] > 1:
                j += 1
            if nums[i] - nums[j] == 1:
                maxLength = max(maxLength, i - j + 1)
        return maxLength


# Example run
if __name__ == "__main__":
    test_input = [1, 3, 2, 2, 5, 2, 3, 7]
    print("Output:", Solution().findLHS(test_input))

