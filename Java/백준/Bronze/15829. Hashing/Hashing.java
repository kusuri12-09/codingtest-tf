import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        String str = sc.next();
        int hash = 0;
        int pow = 1;

        for (int i = 0; i < n; i++) {
            hash += (str.charAt(i) - 'a' + 1) * pow;
            pow *= 31;
        }

        System.out.println(hash);
    }
}
