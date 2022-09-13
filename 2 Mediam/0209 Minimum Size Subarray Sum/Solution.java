import java.util.*;

public class Solution {

    // Brute Force (TLE)
    // O(N^2) O(1)
    public int minSubArrayLen1(int target, int[] nums) {
        int n = nums.length, ans = n + 1;

        for (int start = 0; start < n; start++) {
            int sum = 0;
            for (int end = start; end < n; end++) {
                sum += nums[end];
                if (sum >= target) {
                    ans = Math.min(ans, end - start + 1);
                    break;
                }
            }
        }

        return ans == n + 1 ? 0 : ans;
    }

    // Two Pointers
    // O(N) O(1)
    public static int minSubArrayLen2(int target, int[] nums) {
        int n = nums.length, ans = n + 1;
        int low = 0, high = 0, sum = 0;

        while (high < n) {
            sum += nums[high++];
            while (sum >= target) {
                ans = Math.min(ans, high - low);
                sum -= nums[low++];
            }
        }
        return ans == n + 1 ? 0 : ans;
    }

    public int minSubArrayLen3(int target, int[] nums) {
        int i = 0, n = nums.length, res = n + 1;
        for (int j = 0; j < n; ++j) {
            target -= nums[j];
            while (target <= 0) {
                res = Math.min(res, j - i + 1);
                target += A[i++];
            }
        }
        return res % (n + 1);
    }

    // Binary Search + Prefix Sum
    // O(NlogN) O(N)
    public int minSubArrayLen(int target, int[] nums) {
        int n = nums.length, ans = n + 1;
        int[] sums = new int[n + 1];

        for (int i = 1; i < n + 1; i++) {
            sums[i] = sums[i - 1] + nums[i - 1];
        }

        for (int i = 1; i < n + 1; i++) {
            int s = sums[i - 1] + target;
            int index = lowerBound(i, sums, s);
            if (index == n + 1) {
                break;
            }
            ans = Math.min(ans, index - i + 1);
        }
        return ans == n + 1 ? 0 : ans;
    }

    private int lowerBound(int l, int[] sums, int s) {
        int r = sums.length - 1;
        while (l <= r) {
            int m = l + (r - l) / 2;
            if (sums[m] >= s) {
                r = m - 1;
            } else {
                l = m + 1;
            }
        }
        return l;
    }
}
