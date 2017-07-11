//set
public static boolean isUnique(String str) {
    Set<Character> set = new HashSet<>();
    for (char ch : str.toCharArray()) {
        if (set.contains(ch)) return false;
        set.add(ch);
    }
    return true;
}

//loop
