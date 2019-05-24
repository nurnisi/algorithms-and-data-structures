    public static List<List<Integer>> generate(int numRows) {
        List<List<Integer>> pt = new ArrayList<>();
        for (int i = 0; i < numRows; i++) {
            List<Integer> lev = new ArrayList<>();
            lev.add(1);
            for (int j = 1; j < i; j++) {
                lev.add(pt.get(i - 1).get(j) + pt.get(i - 1).get(j - 1));
            }
            if (i != 0) lev.add(1);
            pt.add(lev);
        }
        return pt;
    }