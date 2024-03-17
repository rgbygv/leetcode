# [791. 自定义字符串排序][link] (Medium)

[link]: https://leetcode.cn/problems/custom-sort-string/

给定两个字符串 `order` 和 `s` 。 `order` 的所有字母都是 **唯一** 的，并且以前按照一些自定义的顺序排
序。

对 `s` 的字符进行置换，使其与排序的 `order` 相匹配。更具体地说，如果在 `order` 中的字符 `x` 出现字符
`y` 之前，那么在排列后的字符串中， `x` 也应该出现在 `y` 之前。

返回 满足这个性质的 `s` 的任意一种排列 。

**示例 1:**

```
输入: order = "cba", s = "abcd"
输出: "cbad"
解释:
"a"、"b"、"c"是按顺序出现的，所以"a"、"b"、"c"的顺序应该是"c"、"b"、"a"。
因为"d"不是按顺序出现的，所以它可以在返回的字符串中的任何位置。"dcba"、"cdba"、"cbda"也是有效的输出
。
```

**示例 2:**

```
输入: order = "cbafg", s = "abcd"
输出: "cbad"
解释：字符 "b"、"c" 和 "a" 规定了 s 中字符的顺序。s 中的字符 "d" 没有在 order 中出现，所以它的位置是
弹性的。

按照出现的顺序，s 中的 "b"、"c"、"a" 应排列为"b"、"c"、"a"。"d" 可以放在任何位置，因为它没有按顺序排
列。输出 "bcad" 遵循这一规则。其他排序如 "bacd" 或 "bcda" 也是有效的，只要维持 "b"、"c"、"a" 的顺序
。
```

**提示:**

- `1 <= order.length <= 26`
- `1 <= s.length <= 200`
- `order` 和 `s` 由小写英文字母组成
- `order` 中的所有字符都 **不同**