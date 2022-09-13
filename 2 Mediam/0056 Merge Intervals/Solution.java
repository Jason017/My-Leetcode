import java.util.*;

class Solution {
    public int[][] merge(int[][] intervals) {
        List<int[]> res = new ArrayList<>();
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        res.add(intervals[0]);

        for (int i = 1; i < intervals.length; i++) {
            if (i < intervals.length && res.get(res.size() - 1)[1] >= intervals[i][0]) {
                int start = res.get(res.size() - 1)[0];
                int end = Math.max(res.get(res.size() - 1)[1], intervals[i][1]);
                res.remove(res.size() - 1);
                res.add(new int[] { start, end });
            } else {
                res.add(intervals[i]);
            }
        }

        int[][] arr = new int[res.size()][2];
        for (int i = 0; i < res.size(); i++) {
            arr[i] = res.get(i);
        }
        return arr;
    }
}