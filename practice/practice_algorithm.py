class Solution:
    """
    1st practice:Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    """

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False

        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

    def is_palindrome(self, x):
        """
        :argument Determine whether an integer is a palindrome. Do this without extra space.
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x = int(x / 10)

        return x == rev or x == int(rev / 10)


if __name__ == '__main__':
    solution = Solution()
    print("two sum for target: ", solution.twoSum([1, 2, 6, 12, 4], 8))
    print("whether input is palindrome: %r" % solution.is_palindrome(123454321))
