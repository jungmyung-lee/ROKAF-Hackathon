import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;


public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int a = Integer.parseInt(br.readLine());
        
        for (int i=2; i<= a; i++){
            if (a % i ==0){
                while (a % i  == 0){
                    System.out.println(i);
                    a /= i;
       }
                
            }
        }
        
        
    }
}