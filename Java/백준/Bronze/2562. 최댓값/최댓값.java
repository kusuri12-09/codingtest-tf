import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int big = 0, big_num = 0;
        int[] numbers = new int[9];

        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = sc.nextInt();
        }

        for (int i = 0; i < numbers.length; i++) {
            if (big < numbers[i]) {
                big = numbers[i];
                big_num = i + 1;
            }
        }

        System.out.println(big);
        System.out.println(big_num);
    }
}