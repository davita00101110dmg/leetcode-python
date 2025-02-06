class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        products = {}
        result = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                prod = nums[i] * nums[j]
                if prod not in products:
                    products[prod] = []
                products[prod].append((nums[i], nums[j]))

        for prod in products:
            pairs = products[prod]
            pairs_len = len(pairs)
            if pairs_len > 1:
                result += pairs_len * (pairs_len - 1) * 4
        
        return result