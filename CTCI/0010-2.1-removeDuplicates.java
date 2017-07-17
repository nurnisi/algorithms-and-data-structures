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

//recursive
static Set<Integer> set = new HashSet<>();

public static ListNode removeDuplicatesRecursive(ListNode head) {
    if (head == null) return head;
    set.add(head.val);
    helper(head, head.next);
    return head;
}

private static void helper(ListNode prev, ListNode runner) {
    if (runner == null) return;

    if (!set.contains(runner.val)) {
        set.add(runner.val);
        helper(prev.next, runner.next);
    }
    else {
        runner = runner.next;
        prev.next = runner;
        helper(prev, runner);
    }
}

//without buffer
public static void removeDuplicatesWithoutBuffer(ListNode head) {
    if (head == null) return;

    ListNode check = head, prev = head, runner;
    while (check != null && check.next != null) {
        runner = check.next;
        while (runner != null) {
            if (runner.val == check.val) {
                prev.next = runner.next;
                runner = runner.next;
            } else {
                runner = runner.next;
                prev = prev.next;
            }
        }
        check = check.next;
        prev = check;
    }
}
