// 6-3
// 4-3,5-1,2-2,1-3,4-4
// 1-1,3-5,5-2,2-3,2-4
// 1-2,1-2
// 3-2,2-1,1-4,4-4,5-4,4-2,2-1
// 5-5,5-5,4-4,5-5,5-5,5-5,5-5,5-5,5-5,5-5

public static List<Integer> toptalDomino() throws IOException {
    BufferedReader br = new BufferedReader(new FileReader("/Users/Nursultan/Desktop/s.txt"));
    String line = br.readLine();
    List<String> inputs = new ArrayList<>();
    while(line != null) {
        inputs.add(line);
        line = br.readLine();
    }

    List<Integer> result = new ArrayList<>();
    for(String st : inputs) {
        StringTokenizer tokenizer = new StringTokenizer(st, ",");
        List<String> list = new ArrayList<>();
        while(tokenizer.hasMoreTokens()) {
            list.add(tokenizer.nextToken());
        }

        String[] array = new String[list.size()];
        array = list.toArray(array);
        int counter = 1;
        int maximum = counter;
        for(int i = 1; i < array.length; i++) {
            String first = array[i-1];
            String second = array[i];
            if(first.charAt(2) == second.charAt(0)) {
                counter++;
            } else {
                counter = 1;
            }
            maximum = Math.max(maximum, counter);
        }
        result.add(maximum);
    }
    return result;
}
