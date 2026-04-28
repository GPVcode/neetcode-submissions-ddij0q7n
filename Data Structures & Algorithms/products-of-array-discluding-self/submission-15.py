class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output_arr=[]
        # loop through array
        for i, value in enumerate(nums):
            product_holder = 1
            # loop through array to collect product
            for j, value in enumerate(nums):
                if i == j:
                    continue
                else:
                    product_holder *= value
            
            output_arr.append(product_holder)


        return output_arr       