// source: https://leetcode.com/problems/two-sum/
// autor: haoc
// date: 08-12-2015

/* O(n) time complex and O(n) space */
public class Solution {

	public int[] twoSum(int[] nums, int target) {

		int[] res = new int[2];
		int n = nums.length;
		// map tracks integer and its index
		HashMap<Integer, Integer> idxMap = new HashMap<>();

		for (int i = 0; i < n; i++) {

			int cur = nums[i];
			if (idxMap.containsKey(target - cur)) {
				res[0] = idxMap.get(target - cur);
				res[1] = i + 1;
				break;
			} else {
				idxMap.put(cur, i + 1);
			}
		}
		return res;
	}
}
