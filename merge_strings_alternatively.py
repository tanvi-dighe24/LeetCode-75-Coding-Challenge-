# Problem: Merge Strings Alternately
# Link: https://leetcode.com/problems/merge-strings-alternately/
# Approach: Use two pointers and alternate characters
# Time Complexity: O(n + m), Space Complexity: O(n + m)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        result = []

        # Merge characters alternately
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1

        # Add remaining characters
        result.append(word1[i:])
        result.append(word2[j:])

        return "".join(result)
