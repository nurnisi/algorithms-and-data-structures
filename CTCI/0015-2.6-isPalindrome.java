public static boolean isPalindrome(ListNode list) {
    ListNode curr = list, runner = list;
    Deque<Integer> stack = new LinkedList<>();
    while (curr != null) {
        if (runner != null) {
            if (runner.next != null) {
                stack.push(curr.val);
                runner = runner.next.next;
            } else runner = runner.next;
        } else if (stack.pop() != curr.val) return false;
        curr = curr.next;
    }

    return true;
}
