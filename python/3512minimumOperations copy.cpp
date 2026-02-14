#include <iostream>
#include <vector>
#include <numeric>

class Solution {
public:
    int get_number_of_operations(std::vector<int>& nums, int k) {
        return std::accumulate(nums.begin(), nums.end(), 0) % k;
    }
};

int main() {
    std::vector<int> nums = {3, 9, 7};
    int k = 5;

    Solution a1;

    std::cout << a1.get_number_of_operations(nums, k) << std::endl;

    return 0;
}