// Integer
Integer.toString(n);
Integer.toString(n, base);
Integer.valueOf(str);
int n = 5;  // 101
n >> 1;     // 10
n << 1;     // 1010
n & 1;      // 1 (and)
n ^ 1;      // 0 (xor)
Integer.MAX_VALUE; Integer.MIN_VALUE;

// Character
Character.toUpperCase(ch);
Character.toLowerrCase(ch);

// String
char[] charArr = str.toCharArray();
for (char ch : str.toCharArray());
str.charAt(i);
str.length();
String.valueOf(n); 
String.valueOf(charArr); new String(charArr);
str.substring(0, 10);
str.toLowerCase(); str.toUpperCase();
str.split(" ");     // single space
str.split("\\s+");  // multiple whitespaces or tabs

StringBuilder sb = new StringBuilder();
sb.append(str);
sb.toString();
sb.reverse().toString();
sb.deleteCharAt(i);

// Math
Math.max(a, b);
Math.min(a, b);
Math.abs(a);
double p = Math.pow(a, b); // a^b
double sqrt = Math.sqrt(a);

// Array
int[] arr = new int[10];
int[] arr = {1,1};
int[][] arr = new int[2][2]
int[][] arr = {{1,1},{1,1}};
arr.length;
Arrays.sort(arr);
Arrays.sort(arr, (a, b) -> (b[0] - a[0]));
Arrays.fill(arr, 5);
Arrays.toString(arr);
Arrays.asList(str);
int[] temp = arr.clone();

// ArrayList
List<Integer> list = new ArrayList<>();
List<List<Integer>> list2d = new ArrayList<>();
list.size();
list.isEmpty();
list.add(a);
list.get(i);
Collections.reverse(list);
String[] strArr = new String[list.size()];
strArr = list.toArray(res);

// Set
Set<Character> set = new HashSet<>();
set.add(ch);
set.contains(ch);

// Map
Map<Integer,Integer> map = new HashMap<>();
map.put(key, value);
map.containsKey(key);
map.get(key);
map.getOrDefault(key, 0);
for (int key : map.keySet()) map.get(key);

// Stack
Stack<Integer> stack = new Stack<>();
stack.size();
stack.isEmpty();
stack.peek();
stack.push(a);
stack.pop();
Stack<int[]> stack = new Stack<>();
stack.add(new int[]{1,1});

// Queue
Queue<TreeNode> queue = new LinkedList<>();
queue.size();
queue.isEmpty();
queue.peek();
queue.add(node);
queue.remove();

// PriorityQueue (Minheap, Maxheap)
PriorityQueue<Integer> minheap = new PriorityQueue<>();
PriorityQueue<Integer> maxheap = new PriorityQueue<>(Collections.reverseOrder());
pQueue.add(10); 
pQueue.poll();
