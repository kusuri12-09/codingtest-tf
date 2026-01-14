import java.util.Scanner;

public class Main {
    public static final int MOD = 1000000007;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // n * m 격자
        int n = sc.nextInt();
        int m = sc.nextInt();

        // 구멍 칸 수
        int hole = sc.nextInt();

        // 이차원 배열로 시도해보기
        // 아래 짝수 계산하는 부분에서 ArrayIndexOutOfBoundsException 발생하지 않도록 n+2로 선언
        long[][] honeycomb = new long[n+2][m+1];
        for (int i = 0; i <= n+1; i++) {
            for (int j = 0; j <= m; j++) {
                honeycomb[i][j] = 0;
            }
        }  // 0으로 초기화, (1,1)은 1

        honeycomb[1][1] = 1;

        // 구멍 칸 위치 받기
        boolean[][] isHole = new boolean[n+2][m+1];

        for (int i=0;i<hole;i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();

            isHole[x][y] = true;
        }

        // 이차원배열 honeycomb에서 구멍 칸은 0으로 설정
        // 나머지 칸은 점화식으로 그 칸으로 가는 경로의 개수를 구함
        // dp[x][y] = dp[x-1][y] + dp[x][y-1] + dp[x+1][y-1] (y가 짝수)
        // dp[x][y] = dp[x-1][y] + dp[x-1][y-1] + dp[x][y-1] (y가 홀수)
        for (int j=1;j<=m;j++){
            for (int i=1;i<=n;i++){
                if (isHole[i][j]) continue;
                if (i==1 && j==1) continue;

                if (j % 2 == 0) {
                    honeycomb[i][j] = (honeycomb[i - 1][j] + honeycomb[i][j - 1] + honeycomb[i + 1][j - 1]) % MOD;
                } else {
                    honeycomb[i][j] = (honeycomb[i - 1][j] + honeycomb[i - 1][j - 1] + honeycomb[i][j - 1]) % MOD;
                }
            }
        }

        System.out.println(honeycomb[n][m]%MOD);
    }
}
