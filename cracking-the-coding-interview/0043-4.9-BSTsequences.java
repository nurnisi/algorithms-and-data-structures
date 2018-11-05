ArrayList<LinkedList<Integer>> allSequences(TreeNode node) {
    ArrayList<LinkedList<Integer>> result = new ArrayList<>();

    if (node == null) {
        result.add(new LinkedList<Integer>());
        return result;
    }

    LinkedList<Integer> prefix = new LinkedList<>();
    prefix.add(node.data);

    // Recurse on left and right subtrees
    ArrayList<LinkedList<Integer>> leftSeq = allSequences(node.left);
    ArrayList<LinkedList<Integer>> rightSeq = allSequences(node.right);

    // Weave together each list from left and right sides
    for (LinkedList<Integer> left : leftSeq) {
        for (LinkedList<Integer> right : rightSeq) {
            ArrayList<LinkedList<Integer>> weaved = new ArrayList<>();
            weaveLists(left, right, weaved, prefix);
            result.addAll(weaved);
        }
    }

    return result;
}

void weaveLists(LinkedList<Integer> first, LinkedList<Integer> second, 
                ArrayList<LinkedList<Integer>> weaved, LinkedList<Integer> prefix) {
    if (first.size() == 0 || second.size() == 0) {
        LinkedList<Integer> clone = prefix.clone();
        clone.addAll(first);
        clone.addAll(second);
        weaved.add(clone);
        return;
    }

    int headFirst = first.removeFirst();
    prefix.addLast(headFirst);
    weaveLists(first, second, weaved, prefix);
    prefix.removeLast();
    first.addFirst(headFirst);

    int headSecond = second.removeFirst();
    prefix.addLast(headSecond);
    weaveLists(first, second, weaved, prefix);
    prefix.removeLast();
    second.addFirst(headSecond);
}