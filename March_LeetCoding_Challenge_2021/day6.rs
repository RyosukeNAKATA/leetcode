/*
Question: Short Encoding of Words
A valid encoding of an array of words is any reference string s and array of indices indices such that:
- words.length == indices.length
- The reference string s ends with the '#' character.
- For each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i].
Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.
*/
use std::collections::HashSet;
impl Solution {
    pub fn minimum_length_encoding(words: Vec<String>) -> i32 {
        let word_set: HashSet<String> = words.into_iter().collect();
        for word in words {
            if word_set.contains(word) {
                for i in 1..word.len() {
                    word_set.remove(word[i..]);
                }
            }
        }
        return 
    }
}