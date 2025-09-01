from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if both strings can be formed by a common base
        if str1 + str2 != str2 + str1:
            return ""
        
        # The GCD length determines the repeating pattern
        length = gcd(len(str1), len(str2))
        return str1[:length]
