/*
Question: Distribute Candies
Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor.
The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice.
Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.
*/
use std::collections::HashSet;
impl Solution {
    pub fn distribute_candies(candy_type: Vec<i32>) -> i32 {
        let available: i32 = (candy_type.len() as i32) / 2;
        let hash_candy: HashSet<i32> = candy_type.into_iter().collect();
        let types: i32 = hash_candy.len() as i32;
        if available >= types {
            return types
        } else {
            return available
        }
    }
}