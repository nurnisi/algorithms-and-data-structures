import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(longestWord2(new String[]{"w","wo","wor","worl", "world"}));
    }

    //trie solution
    class Node {
        char c;
        Map<Character, Node> children = new HashMap<>();
        int end;
        public Node(char c) { this.c = c; }
    }

    class Trie {
        Node root;
        String[] words;
        public Trie() { root = new Node('0'); }

        public void insert(String word, int index) {
            Node cur = root;
            for (char c : word.toCharArray()) {
                cur.children.putIfAbsent(c, new Node(c));
                cur = cur.children.get(c);
            }
            cur.end = index;
        }

        public String dfs() {
            String ans = "";
            Stack<Node> stack = new Stack<>();
            stack.push(root);
            while (!stack.isEmpty()) {
                Node node = stack.pop();
                if (node.end > 0 || node == root) {
                    if (node != root) {
                        String word = words[node.end - 1];
                        if (word.length() > ans.length()
                                || (word.length() == ans.length() && word.compareTo(ans) < 0)) {
                            ans = word;
                        }
                    }
                    for (Node n : node.children.values())
                        stack.push(n);
                }
            }
            return ans;
        }
    }

    public String longestWord(String[] words) {
        Trie trie = new Trie();
        int index = 0;
        for (String word : words) {
            trie.insert(word, ++index);
        }
        trie.words = words;
        return trie.dfs();
    }

    //my solution
    public static String longestWord2(String[] words) {
        Arrays.sort(words);
        Set<String> set = new HashSet<>();
        set.add("");
        String ans = "";
        for (String w : words) {
            if (set.contains(w.substring(0, w.length() - 1))){
                set.add(w);
                if (w.length() > ans.length()) ans = w;
            }
        }
        return ans;
    }
}