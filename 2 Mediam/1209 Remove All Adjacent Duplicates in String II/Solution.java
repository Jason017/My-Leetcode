import java.util.*;

public class Solution {
    // Solution 1: Stack
    // O(N) O(N)
    public String removeDuplicates1(String s, int k) {
        Stack<int[]> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (!stack.isEmpty() && stack.peek()[0] == c) {
                stack.peek()[1]++;
            } else {
                stack.push(new int[] { c, 1 });
            }

            while (!stack.isEmpty() && stack.peek()[1] == k) {
                stack.pop();
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int[] pair : stack) {
            for (int i = 0; i < pair[1]; i++) {
                sb.append((char) pair[0]);
            }
        }
        return sb.toString();
    }

    // Solution 2: Optimized Stack Solution
    // O(N) O(N)
    public String removeDuplicates2(String s, int k) {
        Stack<Integer> count = new Stack<>();
        StringBuilder sb = new StringBuilder(s);
        for (int i = 0; i < sb.length(); i++) {
            if (i == 0 || sb.charAt(i) != sb.charAt(i - 1)) {
                count.push(1);
            } else {
                int top = count.pop() + 1;
                if (top == k) {
                    sb.delete(i - k + 1, i + 1);
                    i = i - k;
                } else {
                    count.push(top);
                }
            }
        }
        return sb.toString();
    }

    // Solution 3: Memoise Count
    // O(N) O(N)
    public String removeDuplicates3(String s, int k) {
        StringBuilder sb = new StringBuilder(s);
        int count[] = new int[sb.length()];
        for (int i = 0; i < sb.length(); i++) {
            if (i == 0 || sb.charAt(i) != sb.charAt(i - 1)) {
                count[i] = 1;
            } else {
                count[i] = count[i - 1] + 1;
                if (count[i] == k) {
                    sb.delete(i - k + 1, i + 1);
                    i = i - k;
                }
            }
        }
        return sb.toString();
    }
}
