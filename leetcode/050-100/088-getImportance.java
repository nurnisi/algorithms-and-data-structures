import java.util.*;

public class leetcode {

    public static void main(String[] args) {

    }

    //leetcode solution: DFS recursive
    Map<Integer, Employee> map;
    public int getImportance(List<Employee> employees, int id) {
        map = new HashMap<>();
        for (Employee e : employees) map.put(e.id, e);
        return dfs(id);
    }

    public int dfs(int eid) {
        Employee emp = map.get(eid);
        int ans = emp.importance;
        for (int i : emp.subordinates)
            ans += dfs(i);
        return ans;
    }

    class Employee {
        // It's the unique id of each node;
        // unique id of this employee
        public int id;
        // the importance value of this employee
        public int importance;
        // the id of direct subordinates
        public List<Integer> subordinates;
    }

    //my solution: DFS iterative
    public int getImportance2(List<Employee> employees, int id) {
        Map<Integer, Employee> map = new HashMap<>();
        for (Employee e : employees) map.put(e.id, e);

        Queue<Employee> queue = new LinkedList<>();
        queue.add(map.get(id));
        int ans = 0;

        while (!queue.isEmpty()) {
            Employee emp = queue.poll();
            ans += emp.importance;
            for (int i : emp.subordinates) queue.add(map.get(i));
        }

        return ans;
    }
}
