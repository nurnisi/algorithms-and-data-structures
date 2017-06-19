public String[] findWords(String[] words) {
        char[] first = {'q','w','e','r','t','y','u','i','o','p'};
        char[] second = {'a','s','d','f','g','h','j','k','l'};
        char[] third = {'z','x','c','v','b','n','m'};
        HashMap<Character, Integer> hm = new HashMap<Character, Integer>();
        for(int i = 0; i < first.length; i++) {
            hm.put(first[i], 1);
            if(i < second.length) hm.put(second[i], 2);
            if(i < third.length) hm.put(third[i], 3);
        }

        ArrayList<String> tempRes = new ArrayList<String>();
        for(int j = 0; j < words.length; j++) {
            String str = words[j].toLowerCase();
            int row = hm.get(str.charAt(0));
            boolean check = true;
            for(int k = 1; k < str.length(); k++) {
                if(row != hm.get(str.charAt(k))) {
                    check = false;
                    break;
                }
            }
            if(check) tempRes.add(words[j]);
        }

        String[] res = new String[tempRes.size()];
        res = tempRes.toArray(res);

        return res;
    }
