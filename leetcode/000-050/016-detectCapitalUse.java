public boolean detectCapitalUse(String word) {
    if(word.length() == 1) return true;

    int check;
    if(word.charAt(0) - 'a' >= 0) check = 1;
    else if((word.charAt(1)) - 'a' >= 0) check = 0;
    else check = -1;

    for(int i = 1; i < word.length(); i++) {
        if(check == 1 && word.charAt(i) - 'a' < 0) return false;
        else if(check == 0 && word.charAt(i) - 'a' < 0) return false;
        else if(check == -1 && word.charAt(i) - 'a' >= 0) return false;
    }

    return true;
}

public boolean detectCapitalUse(String word) {
    int capitals = 0;
    for(char ch : word.toCharArray()) if('Z' - ch >= 0) capitals++;
    return (capitals == 0 || capitals == word.length() || (capitals == 1 && 'Z' - word.charAt(0) >= 0));
}
