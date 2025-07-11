import string

class Solution(object):
    def kthCharacter(self, k, operations):
        l = len(operations)
        o = []
        count = 2 ** l
        i = l - 1
        while count > 1:
            if k > count / 2:
                k = k - count / 2
                o.append(operations[i])
            count /= 2
            i = i - 1
        c = o.count(1) % 26
        return string.ascii_lowercase[c]

# 🔍 Test cases
sol = Solution()

# Test 1
print(sol.kthCharacter(4, [0, 1]))  # Expected: 'b'

# Test 2
print(sol.kthCharacter(1, [1, 0, 1]))  # Expected: 'a'

# Test 3
print(sol.kthCharacter(8, [1, 1, 1]))  # Expected: 'd'
