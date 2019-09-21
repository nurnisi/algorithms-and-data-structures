// 17. Letter Combinations of a Phone Number
class Solution {
    String[] map = new String[]{"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    
    public List<String> letterCombinations(String digits) {
        if (digits.isEmpty()) return new ArrayList<>();;
        List<String> ans = new ArrayList<>();
        helper(digits, 0, digits.length(), "", ans);
        return ans;
    }
    
    public void helper(String digits, int i, int n, String cur, List<String> ans) {
        if (i == n) {
            ans.add(cur);
            return;
        }
        
        for (char ch : map[digits.charAt(i) - '2'].toCharArray()) {
            helper(digits, i+1, n, cur + ch, ans);
        }
    }
}