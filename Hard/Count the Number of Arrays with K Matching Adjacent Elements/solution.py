MOD = 10 ** 9 + 7
N = 10 ** 5 + 4

def bigpow(a, n):
    if n == 0:
        return 1
    b = bigpow(a, n // 2)
    b = b * b % MOD
    if n % 2 == 1:
        b = b * a % MOD
    return b

def inv(a):
    return bigpow(a, MOD - 2)

# Precompute factorials and inverse factorials
fs = [1, 1]
inv_fs = [1, 1]
for i in range(2, N):
    fs.append(fs[-1] * i % MOD)
    inv_fs.append(inv(fs[-1]))

def C(n, k):
    if k < 0 or k > n:
        return 0
    return fs[n] * inv_fs[k] % MOD * inv_fs[n - k] % MOD

class Solution(object):
    def countGoodArrays(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        return C(n - 1, k) * m % MOD * bigpow(m - 1, n - k - 1) % MOD


# 🔁 Test Case
if __name__ == "__main__":
    sol = Solution()
    print(sol.countGoodArrays(5, 3, 2))  # Example usage
