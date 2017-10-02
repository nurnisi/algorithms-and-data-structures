static double boysAndGirls(int n) {
    int girls = 0;
    int boys = 0;
    for (int i = 0; i < n; i++) {
        int[] gender = runOneFamily();
        girls += gender[0];
        boys += gender[1];
    }
    return girls / (double) (boys + girls);
}

static int[] runOneFamily() {
    Random random = new Random();
    int boys = 0;
    int girls = 0;
    while (girls == 0) {
        if (random.nextBoolean()) girls++;
        else boys++;
    }
    int[] gender = {girls, boys};
    return gender;
}