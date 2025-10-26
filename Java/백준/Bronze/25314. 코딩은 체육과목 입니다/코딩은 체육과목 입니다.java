import java.util.*; 
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int a = Integer.parseInt(br.readLine());
        
        String s ="";
        for (int i=0; i< (a/4) ; i++){
            s += "long ";
            
        }
        
        s += "int";
        
        System.out.println(s);
        
        
        
        
        
        
    }

}