class Solution:
    def predictTheWinner(self, nums):
        dp = nums[:]

        for length in range(2, len(nums) + 1):
            for i in range(len(nums) - length + 1):
                j = i + length - 1

                left = nums[i] - dp[i + 1]
                right = nums[j] - dp[i]

                dp[i] = max(left, right)

        return dp[0] >= 0