import java.util.*;

public class GuessMyNumber {
    public static void main(String[] args) {
        // initialize variables
        Scanner scanner = new Scanner(System.in);
        String response = "";
        int high = 0, low = 0;
        int guess = (low + high) / 2;

        // ask user for range of numbers
        System.out.print("Enter n: ");
        int n = scanner.nextInt();
        // asks user for positive integer if 0 or a negative is entered
        while (n < 1) {
            System.out.print("Enter a positive integer for n:");
            n = scanner.nextInt();
        }
        high = n;

        // asks user to pick a number between 0 and n-1
        System.out.println("Welcome to Guess My Number!\nPlease think of a number between 0 and " + (n - 1) + ".");

        // computer will continue to guess the midpoint of the available numbers until
        // the correct answer is given
        while (!(response.equalsIgnoreCase("C"))) {
            guess = (low + high) / 2;
            System.out.println("Is your number: " + guess + "?");
            System.out.println("Please enter C for correct, H for too high, or L for too low.");
            System.out.print("Enter your response (H/L/C): ");
            response = scanner.next();

            // if the user's number is higher than the made guess, low becomes guess+1
            if (response.equalsIgnoreCase("H")) {
                low = guess + 1;
            }
            // if the user's number is higher than the made guess, low becomes guess+1
            else if (response.equalsIgnoreCase("L")) {
                high = guess - 1;
            }
            // if the user's number matches the made guess the game ends
            else if (response.equalsIgnoreCase("C")) {
                System.out.println("Thank you for playing Guess My Number!");
            }
        }
        scanner.close();
    }
}
