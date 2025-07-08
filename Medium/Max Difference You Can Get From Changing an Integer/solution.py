class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = str(num)

        # Find max possible number by replacing first non-9 digit with 9
        for ch in num_str:
            if ch != '9':
                max_digit_to_replace = ch
                break
        else:
            max_digit_to_replace = None 
        if max_digit_to_replace:
            max_str = num_str.replace(max_digit_to_replace, '9')
        else:
            max_str = num_str

        # Find min possible number by replacing digit with 1 or 0
        if num_str[0] != '1':
            min_digit_to_replace = num_str[0]
            min_str = num_str.replace(min_digit_to_replace, '1')
        else:
            for ch in num_str[1:]:
                if ch != '0' and ch != '1':
                    min_digit_to_replace = ch
                    min_str = num_str.replace(min_digit_to_replace, '0')
                    break
            else:
                min_str = num_str

        return int(max_str) - int(min_str)


# 🚀 Example Test Case
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxDiff(9288))  # Output: 8700
