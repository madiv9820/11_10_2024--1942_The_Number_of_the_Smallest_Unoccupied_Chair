# 1942. The Number of the Smallest Unoccupied Chair

__Type:__ Medium <br>
__Topics:__ Array, Hash Table, Heap (Priority Queue) <br>
__Companies:__ Amazon, Microsoft, Otter.ai <br>
__Leetcode Link:__ [The Number of the Smallest Unoccupied Chair](https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description/)
<hr>

There is a party where `n` `friends` numbered from `0` to `n - 1` are attending. There is an infinite number of chairs in this party that are numbered from `0` to `infinity`. When a friend arrives at the party, they sit on the unoccupied chair with the __smallest number__.

- For example, if chairs `0`, `1`, and `5` are occupied when a friend comes, they will sit on chair number `2`.

When a friend leaves the party, their chair becomes unoccupied at the moment they leave. If another friend arrives at that same moment, they can sit in that chair.

You are given a __0-indexed__ 2D integer array `times` where <code>times[i] = [arrival<sub>i</sub>, leaving<sub>i</sub>]</code>, indicating the arrival and leaving times of the <code>i<sup>th</sup></code> friend respectively, and an integer `targetFriend`. All arrival times are __distinct__.

Return _the __chair number__ that the friend numbered_ `targetFriend` _will sit on_.
<hr>

### Examples:

__Example 1:__ <br>
__Input:__ times = [[1,4],[2,3],[4,6]], targetFriend = 1 <br>
__Output:__ 1 <br>
__Explanation:__ <br> - Friend 0 arrives at time 1 and sits on chair 0.- Friend 1 arrives at time 2 and sits on chair 1.<br> - Friend 1 leaves at time 3 and chair 1 becomes empty.<br> - Friend 0 leaves at time 4 and chair 0 becomes empty.<br> - Friend 2 arrives at time 4 and sits on chair 0. <br><br>
Since friend 1 sat on chair 1, we return 1.

__Example 2:__ <br>
__Input:__ times = [[3,10],[1,5],[2,6]], targetFriend = 0 <br>
__Output:__ 2 <br>
__Explanation:__ <br> - Friend 1 arrives at time 1 and sits on chair 0. <br> - Friend 2 arrives at time 2 and sits on chair 1. <br> - Friend 0 arrives at time 3 and sits on chair 2. <br> - Friend 1 leaves at time 5 and chair 0 becomes empty. <br> - Friend 2 leaves at time 6 and chair 1 becomes empty. <br> - Friend 0 leaves at time 10 and chair 2 becomes empty. <br><br>
Since friend 0 sat on chair 2, we return 2.
<hr>

### Constraints:

- `n == times.length`
- <code>2 <= n <= 10<sup>4</sup></code>
- `times[i].length == 2`
- <code>1 <= arrival<sub>i</sub> < leaving<sub>i</sub> <= 10<sup>5</sup></code>
- `0 <= targetFriend <= n - 1`
- Each <code>arrival<sub>i</sub></code> time is __distinct__.
<hr>

### Hints
- Sort times by arrival time.
- for each arrival_i find the smallest unoccupied chair and mark it as occupied until leaving_i.