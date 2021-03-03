class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for num in nums:
            for i in range(1, len(nums)-nums.index(num)):
                print(num + nums[nums.index(num)+i])
                if num + nums[nums.index(num)+i] == target:
                    print("[" + str(nums.index(num)) +
                          "," + str(nums.index(num)+i) + "]")
                    return [nums.index(num), nums.index(num)+i]


if __name__ == "__main__":
    sol = Solution()
    sol.twoSum([3, 2, 4], 6)
