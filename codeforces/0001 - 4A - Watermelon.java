import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        
        int a = reader.nextInt();
        if(a==2){
            System.out.println("NO");
        }
        else if(a%2==0){
            System.out.println("YES");
        }
        else{
            System.out.println("NO");
        }
        
        
    }    
}