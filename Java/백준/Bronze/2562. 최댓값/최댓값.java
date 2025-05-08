import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int big = 0, big_num = 0;

        for (int i = 1; i <= 9; i++) {
            int num = sc.nextInt();
            if (big < num) {
                big = num;
                big_num = i;
            }
        }

        System.out.println(big);
        System.out.println(big_num);
    }
}