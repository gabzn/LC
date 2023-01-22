https://leetcode.com/problems/factor-combinations/description/

class Solution {
    public List<List<Integer>> getFactors(int n) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> current = new ArrayList<>();
        backtrack(n, 2, current, res);
        return res;
    }

    public void backtrack(int n, int start, List<Integer> current, List<List<Integer>> res) {
        if (n == 1) {
            if (current.size() > 1) res.add(new ArrayList<>(current));
            return;
        }

        for(int i=start; i<=n; i++) {
            if (n % i == 0) {
                current.add(i);
                backtrack(n / i, i, current, res);
                current.remove(current.size() - 1);
            }
        }
    }
}
