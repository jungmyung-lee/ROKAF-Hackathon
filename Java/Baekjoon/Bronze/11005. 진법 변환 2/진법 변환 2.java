import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        String S = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        
        int n = sc.nextInt();
        int b = sc.nextInt();
        StringBuilder sb = new StringBuilder();
        
        while (n!=0){
            sb.append( S.charAt(n % b) );
            n /= b;
        }
        
        
        System.out.println(sb.reverse());
    }
}