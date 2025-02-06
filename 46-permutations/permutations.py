class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.permute_helper([], set(), nums, result)
        return result 

    def permute_helper(self, curr_perm: List[int], used: Set[int], nums: List[int], result: List[List[int]]) -> None:
        if len(curr_perm) == len(nums):
            result.append(curr_perm.copy())

        for num in nums:
            if num not in used:
                used.add(num)
                curr_perm.append(num)
                self.permute_helper(curr_perm, used, nums, result)
                curr_perm.pop()
                used.remove(num)
