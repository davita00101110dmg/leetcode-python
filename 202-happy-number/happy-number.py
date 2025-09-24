class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 or n == 7:
            return True
        else:
            sum = n
            while sum > 9:
                str_sum = str(sum)
                sum = 0
                for num in str_sum:
                    sum += int(num) ** 2
                    print(sum)
                if sum == 1 or sum == 7:
                    return True
            return False