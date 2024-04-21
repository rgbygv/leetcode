# [100291. Count the Number of Special Characters II][link] (Medium)

[link]: https://leetcode.cn/contest/weekly-contest-394/problems/count-the-number-of-special-characters-ii/

You are given a string `word`. A letter `c` is called **special** if it appears **both** in
lowercase and uppercase in `word`, and **every** lowercase occurrence of `c` appears before the
**first** uppercase occurrence of `c`.

Return the number of **special** lettersin `word`.

**Example 1:**

**Input:** word = "aaAbcBC"

**Output:** 3

**Explanation:**

The special characters are `'a'`, `'b'`, and `'c'`.

**Example 2:**

**Input:** word = "abc"

**Output:** 0

**Explanation:**

There are no special characters in `word`.

**Example 3:**

**Input:** word = "AbBCab"

**Output:** 0

**Explanation:**

There are no special characters in `word`.

**Constraints:**

- `1 <= word.length <= 2 * 10⁵`
- `word` consists of only lowercase and uppercase English letters.
