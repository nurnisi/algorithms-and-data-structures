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

//reverse ctci solution
//reverse
public static boolean isPalindromeReverse(ListNode head) {
    ListNode reversed = reverseAndClone(head);
    return isEqual(head, reversed);
}

public static ListNode reverseAndClone(ListNode node) {
    ListNode head = null;
    while (node != null) {
        ListNode n = new ListNode(node.val);
        n.next = head;
        head = n;
        node = node.next;
    }
    return head;
}

public static boolean isEqual(ListNode one, ListNode two) {
    while (one != null && two != null) {
        if (one.val != two.val) return false;
        one = one.next;
        two = two.next;
    }
    return one == null && two == null;
}
