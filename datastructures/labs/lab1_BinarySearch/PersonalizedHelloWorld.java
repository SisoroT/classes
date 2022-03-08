import java.util.*;

public class PersonalizedHelloWorld {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("What is your name?");
        String name = scanner.nextLine();
        while (name.equals("")) {
            System.out.println("What is your name?");
            name = scanner.nextLine();
        }
        System.out.println("Hello " + name + "!");
        scanner.close();
    }
}
