class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        while len(x) >= 1:
            if x[0] == x[-1]:
                x = x[1:-1]
                if len(x) <= 1:
                    return True
            else:
                return False
                break