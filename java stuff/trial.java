import java.util.*;
import java.util.Scanner;


//playing around with multiplication problems from SPOJ,
//asking user for no. of test case and then getting the numbers to be multiplied and then printing the answer
public class trial{
    public static void main(String[] args){
        int ans;
        Scanner testCase = new Scanner(System.in).useDelimiter("[,\\s+]");
        String testCaseNo = testCase.nextLine();
        for(int j = 0; j<Integer.parseInt(testCaseNo); j++){
            Scanner input = new Scanner(System.in).useDelimiter("[,\\s+]");
            String s = input.nextLine();
            String[] numbers = s.split(" ");
            for(int i =0; i<numbers.length - 1; i++){
                ans = Integer.parseInt(numbers[i]) * Integer.parseInt(numbers[i+1]);
                System.out.println(ans);
            }
        }
        
    }
}
