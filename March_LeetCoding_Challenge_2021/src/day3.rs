/*
Question: Missing Number
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
*/
impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let mut sum_vec: i32 = 0;
        for s in nums.iter() {
            sum_vec += s;
        }
        let diff_sum: i32 = (nums.len() as i32) * ((nums.len() as i32) + 1) / 2 - sum_vec as i32;
        return diff_sum
    }
}