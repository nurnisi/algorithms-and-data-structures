public int findLUSlength(String a, String b) {
    Set<Character> A = new HashSet<>();
    Set<Character> B = new HashSet<>();

    for(int i = 0; i < a.length(); i++) A.add(a.charAt(i));
    for(int j = 0; j < b.length(); j++) B.add(b.charAt(j));

    int LUS = 0, counter = 0;
    for(int i = 0; i < a.length(); i++) {
        if(!B.contains(a.charAt(i))) {
            LUS = Math.max(LUS, ++counter);
        } else counter = 0;
    }
    counter = 0;
    for(int j = 0; j < b.length(); j++) {
        if(!A.contains(b.charAt(j))) {
            LUS = Math.max(LUS, ++counter);
        } else counter = 0;
    }
    if(LUS == 0) return -1;
    return LUS;
}
