/*
Question.
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
You are given an integer array nums representing the data status of this set after the error.
Find the number that occurs twice and the number that is missing and return them in the form of an array.
*/
use std::vec;
// use std::iter::Sum;
impl Solution {
    pub fn find_error_nums(nums: Vec<i32>) -> Vec<i32> {
        let mut output: Vec<i32> = Vec::new();
        let mut list: Vec<i32> = Vec::new();
        let mut sum = 0;
        for i in nums.iter() {
            sum += nums;
        }
        let diff_sum: i32 = nums.len() * (nums.len() + 1) / 2 - sum;
        for num in nums.iter() {
            if num in list {
                output.push(num)
                output.push(num+diff_sum)
                break
            }
            list.push(num)
        }
        return output;
    }
}