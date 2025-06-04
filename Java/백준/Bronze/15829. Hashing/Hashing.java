import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        String str = sc.next();
        long sum = 0;
        long pow = 1;

        for (int i = 0; i < n; i++) {
            sum += ((str.charAt(i) - 'a' + 1) * pow);
            pow = (pow * 31) % 1234567891;
        }

        System.out.println(sum % 1234567891);
    }
}
