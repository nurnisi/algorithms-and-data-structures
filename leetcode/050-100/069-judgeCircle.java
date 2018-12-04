public static boolean judgeCircle(String moves) {
    int ud = 0, lr = 0;
    for (char c : moves.toCharArray()) {
        if (c == 'U') ud++;
        else if (c == 'D') ud--;
        else if (c == 'L') lr++;
        else if (c == 'R') lr--;
    }
    return ud == 0 && lr == 0;
}
