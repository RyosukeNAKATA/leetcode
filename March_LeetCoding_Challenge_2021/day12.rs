"""
Question: Check If a String Contains All Binary Codes of Size K
Given a binary string s and an integer k.
Return True if every binary code of length k is a substring of s. Otherwise, return False.
"""
use std::collections::HashSet;
impl Solution {
    pub fn has_all_codes(s: String, k: i32) -> bool {
        let mut set_list = HashSet::new();
        // let ss: &str = &s;
        for i in 0..(&s.len() as i32 - k + 1) {
            set_list.insert(&s[i .. i+k]);
        }
        if set_list.len() == 2.pow(k) {
            return true
        } else {
            return false
        }
    }
}

// fn type_of<T>(_: T) -> String{
//     let a = std::any::type_name::<T>();
//     return a.to_string();
//     }