class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        l = k - len(s) % k
        ret = []
        for i in range(0, len(s) - (k - l), k):
            ret.append(s[i:i + k])
        if l != k:
            ret.append(s[len(s) - (k - l):] + fill * l)
        return ret

# 🧪 Example Test Case
if __name__ == "__main__":
    s = "abcdefghi"
    k = 3
    fill = "x"
    obj = Solution()
    print(obj.divideString(s, k, fill))  # Output: ['abc', 'def', 'ghi']
