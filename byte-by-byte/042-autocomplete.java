/* 
 * Write an autocomplete class that returns all dictionary words with a given prefix.
 *  
 * Example: 
 * dict:   {"abc", "acd", "bcd", "def", "a", "aba"}
 *
 * prefix: "a" -> "abc", "acd", "a", "aba"
 * prefix: "b" -> "bcd"
 */

class Autocomplete {
    private class Node {
        String prefix;
        Map<Character, Node> children;
        boolean isWord; // Does this node represent the last character in a word?

        public Node(String prefix) {
            this.prefix = prefix;
            this.children = new HashMap<>();
        }
    }

    // The trie
    private Node trie;

    // Construct the trie from the dictionary
    public Autocomplete(String[] dict) {
        trie = new Node("");
        for (String s: dict) insertWord(s);
    }

    // Insert a word into the trie
    private void insertWord(String s) {
        // Iterate through each character in the string. If the character is not
        // already in the trie then add it
        Node curr = trie;
        for (int i = 0; i < s.length(); i++) {
            if (!curr.children.containsKey(s.charAt(i))) {
                curr.children.put(s.charAt(i), new Node(s.substring(0, i + 1)));
            }
            curr = curr.children.get(s.charAt(i));
            if (i == s.length() - 1) curr.isWord = true;
        }
    }

    // Find all words in trie that start with prefix
    public List<String> getAllWordsForPrefix(String pre) {
        List<String> results = new ArrayList<>();

        // Iterate to the end of the prefix
        Node curr = trie;
        for (char c : pre.toCharArray()) {
            if (curr.children.containsKey(c)) curr = curr.children.get(c);
            else return results;
        }

        // At the end of the prefix, find all child words
        findAllChildWords(curr, results);
        return results;
    }

    private void findAllChildWords(Node n, List<String> results) {
        if (n.isWord) results.add(n.prefix);
        for (Character c : n.children.keySet()) {
            findAllChildWords(n.children.get(c), results);
        } 
    }
}