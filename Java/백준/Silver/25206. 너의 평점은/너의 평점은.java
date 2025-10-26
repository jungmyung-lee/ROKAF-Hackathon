import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String[] arr1 = new String[] {"A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F", "P"};
        double[] arr2 = new double[] {4.5, 4.0, 3.5,3.0, 2.5,2.0, 1.5, 1.0, 0.0, 0.0};
        double total = 0;
        double totalq = 0;
        for (int i=0; i<20; i++){
            String s1 = sc.next();
            double q = sc.nextDouble();
            String s = sc.next();
            for (int j=0; j<9;  j++){
                if (s.equals(arr1[j])){
                    total += arr2[j] * q;
                    totalq += q;
                }
            }
            
        }
        System.out.printf("%.6f", total / totalq);
        
    }
}