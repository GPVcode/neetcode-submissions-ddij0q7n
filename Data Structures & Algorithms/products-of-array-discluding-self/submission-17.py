class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array_len = len(nums)
        left_arr = [1] * array_len
        right_arr = [1] * array_len
        output = [1] * array_len

        # build left array
        for i in range(1, array_len):
            left_arr[i] = left_arr[i - 1] * nums[i - 1]

        for i in range(array_len - 2, -1, -1):
            right_arr[i] = right_arr[i + 1] * nums[i + 1]

        for i in range(array_len):
            output[i] = left_arr[i] * right_arr[i]

        return output