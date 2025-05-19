import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] sizes = new int[6];

        for (int i = 0; i < 6; i++) {
            sizes[i] = sc.nextInt();
        }

        int t = sc.nextInt();
        int p = sc.nextInt();

        int tNum = 0;
        for (int size : sizes) {
            tNum += (size + t - 1) / t;
        }

        System.out.println(tNum);
        System.out.println((n / p) + " " + (n % p));
    }
}
