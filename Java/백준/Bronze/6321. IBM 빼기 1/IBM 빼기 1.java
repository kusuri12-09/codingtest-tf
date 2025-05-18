import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            String str = sc.next();
            System.out.println("String #" + (i + 1));
            for (int j = 0; j < str.length(); j++) {
                if (str.charAt(j) == 'Z') {
                    System.out.print('A');
                } else {
                    System.out.print((char)(str.charAt(j) + 1));
                }
            }
            System.out.println();
            System.out.println();
        }
    }
}
