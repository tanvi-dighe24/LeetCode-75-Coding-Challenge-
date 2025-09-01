# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Approach: Hash Map
# Time Complexity: O(n), Space Complexity: O(n)

class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target - num], i]
            hashmap[num] = i

