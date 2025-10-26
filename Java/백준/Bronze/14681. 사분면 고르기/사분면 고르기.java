import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int x = Integer.parseInt(br.readLine());
        int y = Integer.parseInt(br.readLine());
        
        br.close();
        
        System.out.println(((x>0) && (y>0)) ? "1" : ((x>0) && (y<0)) ? "4" : ((x<0) && (y>0)) ? "2" :"3");
    
        
        
        
    }
}