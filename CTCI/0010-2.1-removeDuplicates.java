public static ListNode removeDuplicates(ListNode head) {
        if (head == null) return head;

        Set<ListNode> set = new HashSet<>();
        ListNode newHead = head, runner = head.next;
        set.add(newHead);
        while (runner != null) {
            if (!set.contains(runner)) {
                set.add(runner);
                newHead.next = runner;
            }
            runner = runner.next;
        }

        return newHead;
    }
