
public class sam_gavis {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int test = 11111111;
		countOnesManually(test);
		countOnes(test);
		System.out.println(countByRecursion(test, 0));
	}

	public static int ones(int n) {
		int sum = 0;

		while(n > 0) {
			sum += n & 1;
			n >>= 1;
		}

		return sum;
	}

	public static void countOnes(int n) {
		String binary = Integer.toBinaryString(n);
		int counter = 0;
		for(char ch : binary.toCharArray()) {
			if(ch == '1') counter++;
		}
		System.out.println(counter);
	}

	public static void countOnesManually(int n) {
		if(n == 0) {
			System.out.println(n);
			return;
		}

		int counter = 0;
		while(n != 1) {
			if(n%2 == 1) counter++;
			n /= 2;
		}
		counter++;
		System.out.println(counter);
	}

	public static int countByRecursion(int n, int counter) {
		if(n == 0 || n == 1) return ++counter;
		if(n%2 == 1) counter++;
		return countByRecursion(n / 2, counter);
	}

	public static int factorial(int n) {
		if(n == 1 || n == 0) return 1;
		return n * factorial(n - 1);
	}

}
