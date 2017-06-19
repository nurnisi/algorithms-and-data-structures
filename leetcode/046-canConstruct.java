public static boolean canConstruct(String ransomNote, String magazine) {
    Map<Character, Integer> map = new HashMap<>();
    for(char ch : magazine.toCharArray()) {
        if(map.get(ch) != null) map.put(ch, map.get(ch) + 1);
        else map.put(ch, 1);
    }

    for(char ch : ransomNote.toCharArray()) {
        if(map.get(ch) == null) return false;
        if(map.get(ch) == 0) return false;
        else map.put(ch, map.get(ch) - 1);
    }

    return true;
}
