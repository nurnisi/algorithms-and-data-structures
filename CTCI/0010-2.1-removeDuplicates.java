public static ListNode removeDuplicates(ListNode head) {
    if (head == null) return head;

    Set<Integer> set = new HashSet<>();
    set.add(head.val);
    ListNode prev = head, runner = head.next;
    while (runner != null) {
        if (!set.contains(runner.val)) {
            set.add(runner.val);
            prev = runner;
        }
        else prev.next = runner.next;
        runner = prev.next;
    }

    return head;
}
