import java.util.*;

public class ArraytoInt {
    public static void main(String[] args) {
        String year = "";
        int[] arr = { 1, 9, 8, 9 };
        // add each number in arr one by one as a string to the empty string year
        for (int i : arr) {
            year += i;
        }
        // convert the string year to an integer x
        int x = Integer.valueOf(year);
        // add 1 to x and print it to console
        System.out.println(x + 1);
    }
}
