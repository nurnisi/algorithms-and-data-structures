import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        ListNode l1 = new ListNode(1);
        l1.next = new ListNode(2);
        l1.next.next = new ListNode(4);
        ListNode l2 = new ListNode(1);
        l2.next = new ListNode(3);
        l2.next.next = new ListNode(4);
        System.out.println(mergeTwoLists(l1,l2));
    }

    public static class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }

    //my recursive solution
    public static ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null) return l2;
        else if (l2 == null) return l1;
        else if (l1.val <= l2.val) {
            l1.next = mergeTwoLists(l1.next, l2);
            return l1;
        } else {
            l2.next = mergeTwoLists(l1, l2.next);
            return l2;
        }
    }

    //error
    public static ListNode mergeTwoLists3(ListNode l1, ListNode l2) {
        ListNode res = null, cur = res;
        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                if (res == null) res = new ListNode(l1.val);
                else cur = new ListNode(l1.val);
                l1 = l1.next;
            } else {
                if (res == null) res = new ListNode(l2.val);
                else cur = new ListNode(l2.val);
                l2 = l2.next;
            }
            cur = cur.next;
        }
        if (l1 != null) cur.next = l1;
        else cur.next = l2;
        return res;
    }

    //my non-recursive long solution
    public static ListNode mergeTwoLists2(ListNode l1, ListNode l2) {
        if (l1 == null) return l2;
        else if (l2 == null) return l1;
        ListNode res;
        if (l1.val < l2.val) {
            res = new ListNode(l1.val);
            l1 = l1.next;
        } else {
            res = new ListNode(l2.val);
            l2 = l2.next;
        }
        ListNode cur = res;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                cur.next = new ListNode(l1.val);
                l1 = l1.next;
            } else {
                cur.next = new ListNode(l2.val);
                l2 = l2.next;
            }
            cur = cur.next;
        }
        if (l1 != null) cur.next = l1;
        if (l2 != null) cur.next = l2;
        return res;
    }
}