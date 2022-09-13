public class Solution {

    // Solution 1: DFS
    // Let N be the number of input equations and M be the number of queries
    // O(MN) O(N)
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        int n = queries.size();
        Map<String, Map<String, Double>> g = new HashMap<>();
        Set<String> visited = new HashSet<>();
        double[] res = new double[n];
        for (int i = 0; i < equations.size(); i++) {
            String src = equations.get(i).get(0);
            String dst = equations.get(i).get(1);
            g.putIfAbsent(src, new HashMap<>());
            g.putIfAbsent(dst, new HashMap<>());
            g.get(src).put(dst, values[i]);
            g.get(dst).put(src, 1 / values[i]);
        }

        for (int i = 0; i < queries.size(); i++) {
            res[i] = dfs(g, visited, queries.get(i).get(0), queries.get(i).get(1));
        }
        return res;
    }
    // a -> [b -> 2]
    // b -> [a -> 1/2], [c -> 3]
    // c -> [b -> 1/3]

    // x1: [x2]
    // x2: [x3, x1]
    // x3: [x4, x2]
    // x4: [x5, x3]
    private double dfs(Map<String, Map<String, Double>> g, Set<String> visited, String src, String dst) {
        if (!g.containsKey(src)) {
            return -1.0;
        }
        if (src.equals(dst)) {
            return 1.0;
        }
        if (g.get(src).containsKey(dst)) {
            // System.out.println("1." + src + "->" + dst + ": " + g.get(src).get(dst));
            return g.get(src).get(dst);
        }

        visited.add(src);
        for (String nei : g.get(src).keySet()) {
            if (!visited.contains(nei)) {
                double val = dfs(g, visited, nei, dst);
                // System.out.println("2." + nei + "->" + dst + ": " + val);
                if (val >= 0) {
                    visited.remove(src);
                    return g.get(src).get(nei) * val;
                }
            }
        }
        visited.remove(src);
        return -1.0;
    }
}
