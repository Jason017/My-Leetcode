import java.util.*;

class Solution {
    // Solution 1: DP (Top Down Approach)
    public boolean wordBreak1(String s, List<String> wordDict) {
        int n = s.length();
        boolean[] dp = new boolean[n + 1];
        Set<String> wordSet = new HashSet<>(wordDict);
        dp[n] = true;
        for (int end = n; end >= 1; end--) {
            for (int start = end - 1; start >= 0; start--) {
                if (dp[end] && wordSet.contains(s.substring(start, end))) {
                    dp[start] = true;
                }
            }
        }
        return dp[0];
    }

    // Solution 2: Optimized DP (Bottom Up Approach)
    public boolean wordBreak2(String s, List<String> wordDict) {
        int n = s.length();
        boolean[] dp = new boolean[n + 1];
        Set<String> wordSet = new HashSet(wordDict);
        dp[0] = true;

        int maxLen = 0;
        for (String word : wordDict) {
            maxLen = Math.max(maxLen, word.length());
        }

        for (int end = 0; end <= n; end++) {
            for (int start = end; start >= 0; start--) {
                if (end - start > maxLen) {
                    continue;
                }
                if (dp[start] && wordSet.contains(s.substring(start, end))) {
                    dp[end] = true;
                    break;
                }
            }
        }

        return dp[n];
    }

    // Solution 3-1: BFS
    // O(N^3) O(N)
    public boolean wordBreak3_1(String s, List<String> wordDict) {
        int n = s.length();
        Deque<Integer> q = new ArrayDeque();
        q.addLast(0);
        Set<String> wordSet = new HashSet<>(wordDict);
        Set<Integer> visited = new HashSet<>();

        while (!q.isEmpty()) {
            int l = q.pollFirst();
            if (visited.contains(l)) {
                continue;
            }
            for (int r = l + 1; r < n + 1; r++) {
                if (wordSet.contains(s.substring(l, r))) {
                    if (r == n) {
                        return true;
                    }
                    q.addLast(r);
                }
            }
            visited.add(l);
        }
        return false;
    }

    // Solution 3-2: BFS
    // O(N^3) O(N)
    public boolean wordBreak3_2(String s, List<String> wordDict) {
        int n = s.length();
        Deque<Integer> q = new ArrayDeque();
        q.addLast(n);
        Set<String> wordSet = new HashSet<>(wordDict);
        Set<Integer> visited = new HashSet<>();

        while (!q.isEmpty()) {
            int r = q.pollFirst();
            if (visited.contains(r)) {
                continue;
            }
            for (int l = r - 1; l >= 0; l--) {
                if (wordSet.contains(s.substring(l, r))) {
                    if (l == 0) {
                        return true;
                    }
                    q.addLast(l);
                }
            }
            visited.add(r);
        }
        return false;
    }

    // Solution 4-1: Recursive with memoization (Top Down Approach)
    // O(N^3) O(N)
    public boolean wordBreak4_1(String s, List<String> wordDict) {
        Map<String, Boolean> memo = new HashMap<>();
        Set<String> wordSet = new HashSet<>(wordDict);
        return dfs(wordSet, memo, s);
    }

    private boolean dfs(Set<String> wordSet, Map<String, Boolean> memo, String currStr) {
        if (currStr.length() == 0) {
            return true;
        }
        if (memo.containsKey(currStr)) {
            return memo.get(currStr);
        }

        for (String word : wordSet) {
            if (currStr.startsWith(word) && dfs(wordSet, memo, currStr.substring(word.length()))) {
                memo.put(currStr, true);
                return true;
            }
        }

        memo.put(currStr, false);
        return false;
    }

    // Solution 4-2: Recursive with memoization (Bottom Up Approach)
    // O(N^3) O(N)
    public boolean wordBreak4_2(String s, List<String> wordDict) {
        Map<Integer, Boolean> memo = new HashMap<>();
        Set<String> wordSet = new HashSet<>(wordDict);
        return dfs(wordSet, memo, s, 0);
    }

    private boolean dfs(Set<String> wordSet, Map<Integer, Boolean> memo, String s, int lo) {
        if (lo == s.length()) {
            return true;
        }
        if (memo.containsKey(lo)) {
            return memo.get(lo);
        }

        for (String word : wordSet) {
            int hi = lo + word.length();
            if (hi <= s.length() && word.equals(s.substring(lo, hi)) && dfs(wordSet, memo, s, hi)) {
                memo.put(lo, true);
                return true;
            }
        }

        memo.put(lo, false);
        return false;
    }
}