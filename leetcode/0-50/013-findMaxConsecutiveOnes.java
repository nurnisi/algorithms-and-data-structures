public int findMaxConsecutiveOnes(int[] nums) {
    int counter = 0;
    int ones = 0;
    for(int i : nums) {
        if(i == 1) counter++;
        if(ones < counter) ones = counter;
        if(i == 0) counter = 0;
    }

    return ones;
}
