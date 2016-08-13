
import edu.princeton.cs.algs4.Shell;
public class Point implements Comparable<Point>{
	private int x;
	private int y;

	public Point(int x, int y){
		this.x = x;
		this.y = y;
	}

	@Override
	public int compareTo(Point that) {
		if(this.x > that.x) return 1;
		if(this.x < that.x) return -1;
		if(this.y > that.y) return 1;
		if(this.y < that.y) return -1;
		return 0;
	}

	public static int countIntersections(Point[] a, Point[] b){
		Shell.sort(a);
		Shell.sort(b);

		int count = 0;
		int i = 0, j = 0;
		while(i < a.length && j < b.length){
			if(a[i].compareTo(b[j]) == 0){
				count++;
				i++;
				j++;
			}
			else if(a[i].compareTo(b[j]) < 0) i++;
			else j++;
		}
		return count;
	}

}
