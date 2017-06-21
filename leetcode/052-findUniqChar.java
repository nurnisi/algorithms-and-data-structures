public static int firstUniqChar(String s) {
    Map<Character, Integer> map = new HashMap<>();
    for (int i = 0; i < s.length(); i++) {
        char ch = s.charAt(i);
        if (map.get(ch) != null) map.put(ch, map.get(ch) + 1);
        else map.put(ch, 1);
    }

    for (int i = 0; i < s.length(); i++) {
        if(map.get(s.charAt(i)) == 1) return i;
    }
    return -1;
}
