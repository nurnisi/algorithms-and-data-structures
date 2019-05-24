//with loop
public static int addDigits(int num) {
    if(num / 10 == 0) return num;
    int res = 0;
    while(num != 0) {
        res += num % 10;
        num /= 10;
    }
    return addDigits(res);
}

//O(1) time and space complexity
public static int addDigits(int num) {
  return 1 + (num - 1) % 9;
}
