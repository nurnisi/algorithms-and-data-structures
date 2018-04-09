public String reverseWords(String s) {
    StringTokenizer st = new StringTokenizer(s, " ");
    String res = "";
    while(st.hasMoreTokens()) {
        String str1 = st.nextToken();
        String str2 = "";
        for(int i = str1.length() - 1; i >= 0; i--) {
            str2 += str1.charAt(i);
        }
        res += str2;
        if(st.hasMoreTokens()) res += " ";
    }

    return res;
}
