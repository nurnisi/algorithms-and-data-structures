interface MyInterface {
    void handlePermutation(String str);
}

public class Client implements MyInterface {
    public void handlePermutation(String str) {
        System.out.println(str);
    }
}

public class Permutations {
    public void getPermutations(String str, MyInterface client) {
        client.handlePermutation("here it is: " + str);
    }
}

public class Main {
    public static void main(String[] args) {
        Permutations perm = new Permutations();
        Client client = new Client();
        perm.getPermutations("ABC", client);    
    }
}