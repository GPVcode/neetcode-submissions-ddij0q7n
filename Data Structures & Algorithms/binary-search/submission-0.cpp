class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        int mid = (left + right) / 2;
        // loop while left < right;
        while(left <= right){           
            cout << nums[mid] << endl;
            // else if target is less than nums [mid] then right is nums[mid - 1]
            if(target == nums[mid]){
                return mid;
            } else if (target > nums[mid]){
                left = mid + 1;
                mid = (left + right) / 2;
            } else{
                right = mid - 1;
                mid = (left + right) / 2;
            }
        }
        return -1;
    }
};

// Divide and conquer
// use two pointer and a middle var
