# [3002. 移除后集合的最多元素数][link] (Medium)

[link]: https://leetcode.cn/contest/weekly-contest-379/problems/maximum-size-of-a-set-after-removals/

给你两个下标从 `0` 开始的整数数组 `nums1` 和 `nums2` ，它们的长度都是偶数 ` n` 。

你必须从 `nums1` 中移除 `n / 2` 个元素，同时从 `nums2` 中也移除 `n / 2` 个元素。移除之后，你将 `nums
1` 和 `nums2` 中剩下的元素插入到集合 `s` 中。

返回集合 `s` 可能的 **最多** 包含多少元素。

**示例 1：**

```
输入：nums1 = [1,2,1,2], nums2 = [1,1,1,1]
输出：2
解释：从 nums1 和 nums2 中移除两个 1 。移除后，数组变为 nums1 = [2,2] 和 nums2 = [1,1] 。因此，s = {
1,2} 。
可以证明，在移除之后，集合 s 最多可以包含 2 个元素。
```

**示例 2：**

```
输入：nums1 = [1,2,3,4,5,6], nums2 = [2,3,2,3,2,3]
输出：5
解释：从 nums1 中移除 2、3 和 6 ，同时从 nums2 中移除两个 3 和一个 2 。移除后，数组变为 nums1 = [1,4
,5] 和 nums2 = [2,3,2] 。因此，s = {1,2,3,4,5} 。
可以证明，在移除之后，集合 s 最多可以包含 5 个元素。
```

**示例 3：**

```
输入：nums1 = [1,1,2,2,3,3], nums2 = [4,4,5,5,6,6]
输出：6
解释：从 nums1 中移除 1、2 和 3 ，同时从 nums2 中移除 4、5 和 6 。移除后，数组变为 nums1 = [1,2,3] 
和 nums2 = [4,5,6] 。因此，s = {1,2,3,4,5,6} 。
可以证明，在移除之后，集合 s 最多可以包含 6 个元素。
```

**提示：**

- `n == nums1.length == nums2.length`
- `1 <= n <= 2 * 10⁴`
- `n` 是偶数。
- `1 <= nums1[i], nums2[i] <= 10⁹`