import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int num = 0;

        for (int i = 0; i < 3; i++) {
             String str = sc.nextLine();

             if (str.charAt(0) != 'F' && str.charAt(0) != 'B') {
                 num = Integer.parseInt(str) + 3 - i;
             }
        }

        if (num % 15 == 0) {
            System.out.println("FizzBuzz");
        } else if (num % 3 == 0) {
            System.out.println("Fizz");
        } else if (num % 5 == 0) {
            System.out.println("Buzz");
        } else {
            System.out.println(num);
        }
    }
}
