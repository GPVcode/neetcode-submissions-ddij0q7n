class Solution {
public:
    int search(vector<int>& nums, int target) {
        if (nums.empty()) return -1; // base case or edge case.

        int left = 0;
        int right = nums.size() - 1;
        // loop while left < right;
        while(left <= right){           
            int mid = (left + right) / 2;
            // else if target is less than nums [mid] then right is nums[mid - 1]
            if(target == nums[mid]){
                return mid; // return index
            } else if (target > nums[mid]){
                left = mid + 1;
            } else{
                right = mid - 1;
            }
        }
        return -1;
    }
};

// Divide and conquer
// use two pointer and a middle var
