import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        base2(new int[]{0,0,1});
    }

    public static int[] base2(int[] A) {
        if (A.length == 0) return A;

        int X = getX(A);
        int Y = X < 0 ? X / 2 : (X + 1) / 2;
        System.out.println(Y);

        ArrayList<Integer> res = new ArrayList<>();
        while (Y != 0) {
            int r = Y % -2;
            Y /= -2;
            res.add(Math.abs(r));
        }

        return A;
    }

    public static int getX(int[] A) {
        int X = 0;
        for (int i = 0; i < A.length; i++) {
            X += A[i] * (int)(Math.pow(-2, i));
        }
        return X;
    }

    static String battleShips(int N, String S, String T) {
        //get ships
        ArrayList<String> list = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(S, ",");
        while (st.hasMoreTokens()) list.add(st.nextToken());

        ArrayList<ArrayList<String>> ships = new ArrayList<>();
        for (String s : list) ships.add(getShip(s));

        //get hits
        Set<String> hits = new HashSet<>();
        StringTokenizer st2 = new StringTokenizer(T, " ");
        while (st2.hasMoreTokens()) hits.add(st2.nextToken());

        //count
        int resSunk = 0, resHits = 0;
        for (ArrayList<String> ship : ships) {
            int tempHits = 0;
            for (String pos : ship) if (hits.contains(pos)) tempHits++;
            if (tempHits == ship.size()) resSunk++;
            else if (tempHits < ship.size() && tempHits != 0) resHits++;
        }

        return resSunk + "," + resHits;
    }

    static ArrayList<String> getShip(String S) {
        ArrayList<String> list = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(S, " ");
        while (st.hasMoreTokens()) list.add(st.nextToken());

        ArrayList<String> res = new ArrayList<>();
        if (list.get(0).equals(list.get(1))) res.add(list.get(0));
        else {
            String s1 = list.get(0), s2 = list.get(1);
            res.add(s1);
            res.add(s2);

            int s1int = getInt(s1), s2int = getInt(s2);
            char s1char = getChar(s1), s2char = getChar(s2);
            StringBuilder sb;
            if (s1int != s2int && s1char != s2char) {
                sb = new StringBuilder();
                sb.append(s2int);
                sb.append(s1char);
                res.add(sb.toString());
                sb = new StringBuilder();
                sb.append(s1int);
                sb.append(s2char);
                res.add(sb.toString());
            } else if (s1int != s2int) {
                while (s1int + 1 != s2int) {
                    sb = new StringBuilder();
                    sb.append(++s1int);
                    sb.append(s1char);
                    res.add(sb.toString());
                }
            } else if (s1char != s2char) {
                s1char = (char)(s1char + 1);
                while (s1char != s2char) {
                    sb = new StringBuilder();
                    sb.append(s1int);
                    sb.append(s1char);
                    res.add(sb.toString());
                    s1char = (char)(s1char + 1);
                }
            }
        }

        return res;
    }

    static int getInt(String S) {
        if (S.length() == 2) return S.charAt(0) - '0';
        else return ((S.charAt(0) - '0') * 10) + (S.charAt(1) - '0');
    }

    static char getChar(String S) {
        if (S.length() == 2) return S.charAt(1);
        else return S.charAt(2);
    }

    static int brackets(String S) {
        int c1 = 0, c2 = 0, res = 0;
        for (int i = 0; i < S.length(); i++) {
            if (S.charAt(i) == '(') c1++;
            else c2++;

            if (c1 == c2) res = c1;
            else res = c2;
        }

        return res;
    }

    static int solution2(String S) {
        int count1 = 0, count2 = 0, len = S.length();
        for (int i = 0; i < len; i++) {
            if (S.charAt(i) == '(') count1++;
            else count2++;
        }
        if (count1 == len) return 0;
        else if (count2 == len) return len;

        int j = 0, k = len - 1;
        while (count1 != 0 && count2 != 0) {
            if (S.charAt(j) == '(') count1--;
            else if (S.charAt(j) == ')') count2--;
            j++;

            if (S.charAt(k) == '(') count1--;
            else if (S.charAt(k) == ')') count2--;
            k--;
        }

        if (count2 == 0) return j;
        return k;
    }

    static int solution1(String S) {
        int c1 = 0, c2 = 0;
        for (char ch : S.toCharArray()) {
            if (ch == '(') c1++;
            else c2++;
        }
        if (c1 == S.length()) return 0;
        else if (c2 == S.length()) return S.length();

        int i = 0, j = S.length() - 1;
        while (i < j) {
            if (S.charAt(i) == '(') {
                while (S.charAt(j) != ')' && j > i) j--;
            }
            i++;
        }

        return i - 1;
    }

    static int bracketSplitString(String s) {

        Deque<Character> stack = new LinkedList<>();

        stack.push(s.charAt(0));

        for (int i = 1; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '[' || c == '{' || c == '(') stack.push(c);
            else if (c == ']' && stack.peek() == '[') stack.pop();
            else if (c == '}' && stack.peek() == '{') stack.pop();
            else if (c == ')' && stack.peek() == '(') stack.pop();
            else return 0;
        }

        if (!stack.isEmpty()) return 0;
        return 1;
    }

    static int battleShips2(char[][] board) {
        int count = 0;
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == 'X') {
                    if (i > 0 && board[i - 1][j] == 'X') continue;
                    else if (j > 0 && board[i][j - 1] == 'X') continue;
                    count++;
                }
            }
        }
        return count;
    }
  