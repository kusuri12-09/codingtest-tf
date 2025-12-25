import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        if (n==0) {
            System.out.println(0);
            System.exit(0);
        }

        int[] difficulty = new int[n];
        for (int i=0;i<n;i++) {
            difficulty[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(difficulty);

        // n의 위아래 15% 구하기
        int limit = (int) Math.round(n*0.15);

        int sum = 0;
        for (int i=limit;i<n-limit;i++) {
            sum+=difficulty[i];
        }

        int avg = (int) Math.round((double) sum / (n - limit * 2));

        System.out.println(avg);
        br.close();
    }
}
