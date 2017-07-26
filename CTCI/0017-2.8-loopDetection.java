public static ListNode loopDetection(ListNode list) {
  Set<ListNode> set = new HashSet<>();
  while (list != null) {
    if (!set.contains(list)) set.add(list);
    else return list;
    list = list.next;
  }
  return null;
}
