
public class Permutation{
	public static boolean isPermutation(int[] a, int[] b){
		if(a.length != b.length) return false;
		ShellSort.sort(a);
		ShellSort.sort(b);

		for(int i = 0; i < a.length; i++)
			if(a[i] != b[i])
				return false;

		return true;
	}
}
