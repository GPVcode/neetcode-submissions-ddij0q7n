class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output array
        output_arr = []
        arr_length = len(nums)
        # loop
        for i, value in enumerate(nums):
            left = 0
            right = 0
            # slice for left
            left_arr = nums[slice(i)]
            left = self.getArrProduct(left_arr)
            # slice for right
            right_arr = nums[slice(i+1, arr_length)]
            right = self.getArrProduct(right_arr)
            output_arr.append(left * right)

        return output_arr

    def getArrProduct(self, arr):
        product_output = 1
        for i in arr:
            product_output *= i
        return product_output