/*
Question: Set Mismatch
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
You are given an integer array nums representing the data status of this set after the error.
Find the number that occurs twice and the number that is missing and return them in the form of an array.
*/
impl Solution {
    pub fn find_error_nums(nums: Vec<i32>) -> Vec<i32> {
        let mut output: Vec<i32> = Vec::new();
        let mut list: Vec<i32> = Vec::new();
        let mut sum_vec: i32 = 0;
        for s in nums.iter() {
            sum_vec += s;
        }
        let diff_sum: i32 = (nums.len() as i32) * ((nums.len() as i32) + 1) / 2 - sum_vec as i32;
        for num in nums {
            for l in list.clone() {
                if num == l {
                    output.push(num);
                    output.push(num + diff_sum);
                    return output
                }
            }
            list.push(num);
        }
        return output;
    }
}