import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int num = sc.nextInt();
        int max = 0;
        double sum = 0;
        int score[] = new int[num];

        for (int i = 0; i < num; i++) {
            score[i] = sc.nextInt();
            if (score[i] > max) {
                max = score[i];
            }
        }

        for (int i = 0; i < num; i++) {
            sum += ((double)score[i] / max) * 100;
        }

        System.out.println(sum/num);

    }
}