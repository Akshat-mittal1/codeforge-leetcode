class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        word = 'a'
        while len(word) < k:
            add = ''
            for i in word:
                if i == 'z':
                    add += 'a'
                    continue
                new = chr(ord(i) + 1)
                add += new
            word += add
        return word[k - 1]


if __name__ == "__main__":
    sol = Solution()

    # 🔸 Sample Test Cases
    print(sol.kthCharacter(10))    # Output: 'c'
    print(sol.kthCharacter(5))    # Output: 'b'
