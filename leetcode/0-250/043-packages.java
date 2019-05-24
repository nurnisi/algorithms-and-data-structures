public static List<Integer> packages(int[][] nums) {
    List<Integer> list = new ArrayList<>();
    HashSet<Integer> set = new HashSet<>();
    for (int i = 0; i < nums.length; i++)
        if (nums[i].length == 0) {
            set.add(i);
            list.add(i);
        }

    if(set.isEmpty()) return list;

    int i = 0;
    while(set.size() != nums.length) {
        if(i >= nums.length) i = 0;
        if(set.contains(i)) {
            i++;
            continue;
        }

        for(int j : nums[i])
            if(!set.contains(j)) {
                i++;
                continue;
            }

        list.add(i);
        set.add(i++);
    }

    return list;
}

//Topological sort
public static List<Integer> packages(int[][] nums) {
    Set<Integer> tempMarks = new HashSet<>();
    Set<Integer> permMarks = new HashSet<>();
    List<Integer> results = new LinkedList<>();

    for (int i = 0; i < nums.length; i++) {
        if(!permMarks.contains(i)) visit(i, nums, tempMarks, permMarks, results);
    }

    return results;
}

public static void visit(int i, int[][] nums, Set<Integer> tempMarks, Set<Integer> permMarks, List<Integer> results) {
    if(tempMarks.contains(i)) throw new RuntimeException("Graph is not acyclic");
    if(!permMarks.contains(i)) {
        tempMarks.add(i);
        for(int j : nums[i]) {
            visit(j, nums, tempMarks, permMarks, results);
        }
        permMarks.add(i);
        tempMarks.remove(i);
        results.add(i);
    }
}
