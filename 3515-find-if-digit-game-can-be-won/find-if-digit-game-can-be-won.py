class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        one_digits_sum, two_digits_sum = 0, 0

        for num in nums:
            if num > 9:
                two_digits_sum += num
            else:
                one_digits_sum += num

        return one_digits_sum != two_digits_sum