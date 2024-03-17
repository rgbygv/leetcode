# [100236. 统计以给定字符开头和结尾的子字符串总数][link] (Medium)

[link]: https://leetcode.cn/contest/weekly-contest-389/problems/count-substrings-starting-and-ending-with-given-character/

给你一个字符串 `s` 和一个字符 `c `。返回在字符串 `s` 中并且以 `c` 字符开头和结尾的非空子字符串的总数
。

**示例 1：**

**输入：** s = "abada", c = "a"

**输出：** 6

**解释：** 以 `"a"` 开头和结尾的子字符串有： `"abada"`、 `"abada"`、 `"abada"`、 `"abada"`、 `"abada
"`、 `"abada"`。

**示例 2：**

**输入：** s = "zzz", c = "z"

**输出：** 6

**解释：** 字符串 `s` 中总共有 `6` 个子字符串，并且它们都以 `"z"` 开头和结尾。

**提示：**

- `1 <= s.length <= 10⁵`
- `s` 和 `c` 均由小写英文字母组成。
