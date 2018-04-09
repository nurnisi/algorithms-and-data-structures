public static int numberOfBoomerangs(int[][] points) {
    int boomerangs = 0;
    for (int i = 0; i < points.length; i++) {
        Map<Double, Integer> map = new HashMap<>();
        for (int j = 0; j < points.length; j++) {
            if(i != j) {
                Double distance = distance(points[i], points[j]);
                if (map.containsKey(distance)) map.put(distance, map.get(distance) + 1);
                else map.put(distance, 1);
            }
        }
        for (Integer value : map.values()) {
            if (value > 1) boomerangs += value * (value - 1);
        }
    }

    return boomerangs;
}

public static Double distance(int[] a, int[] b) {
    return Math.sqrt(Math.pow(a[0] - b[0], 2) + Math.pow(a[1] - b[1], 2));
}
