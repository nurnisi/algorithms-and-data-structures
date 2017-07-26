public static ListNode loopDetection(ListNode list) {
  Set<ListNode> set = new HashSet<>();
  while (list != null) {
    if (!set.contains(list)) set.add(list);
    else return list;
    list = list.next;
  }
  return null;
}

//without additional space buffer
public static ListNode loopDetectionWithoutAdditionalSpaceBuffer(ListNode list) {
  if (list == null || list.next == null) return null;

  ListNode current = list, runner = list.next;
  while (current != runner && runner != null && runner.next != null) {
    current = current.next;
    runner = runner.next.next;
  }

  if (runner == null || runner.next == null) return null;

  current = list;
  while (current != runner) {
    current = current.next;
    runner = runner.next;
  }

  return current;
}
