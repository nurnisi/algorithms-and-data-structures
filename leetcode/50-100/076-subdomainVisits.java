    public static List<String> subdomainVisits(String[] cpdomains) {
        Map<String, Integer> map = new HashMap<>();
        for (String str : cpdomains) {
            StringTokenizer tok = new StringTokenizer(str, " ");
            int count = Integer.valueOf(tok.nextToken());
            String domain = tok.nextToken();
            StringBuilder sb = new StringBuilder();

            for (int i = domain.length() - 1; i >= 0; i--) {
                if (domain.charAt(i) - '.' == 0) {
                    StringBuilder temp = new StringBuilder(sb);
                    String cur = temp.reverse().toString();
                    map.put(cur, map.getOrDefault(cur, 0) + count);
                }
                sb.append(domain.charAt(i));
            }
            String cur = sb.reverse().toString();
            map.put(cur, map.getOrDefault(cur, 0) + count);
        }

        List<String> res = new ArrayList<>();
        for (String s : map.keySet()) {
            res.add(map.get(s) + " " + s);
        }
        return res;
    }

    public static List<String> subdomainVisits_2(String[] cpdomains) {
        Map<String, Integer> map = new HashMap<>();
        for (String domain : cpdomains) {
            String[] cpinfo = domain.split("\\s+");
            String[] frags = cpinfo[1].split("\\.");
            int count = Integer.valueOf(cpinfo[0]);
            String cur = "";
            for (int i = frags.length - 1; i >= 0; i--) {
                cur = frags[i] + (i < frags.length - 1 ? "." : "") + cur;
                map.put(cur, map.getOrDefault(cur, 0) + count);
            }
        }

        List<String> res = new ArrayList<>();
        for (String dom : map.keySet())
            res.add(map.get(dom) + " " + dom);
        return res;
    }