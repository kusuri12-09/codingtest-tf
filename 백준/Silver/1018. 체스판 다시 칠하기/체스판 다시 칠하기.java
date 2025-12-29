import java.io.*;

public class Main {
    public static int getCount(int row, int col, String[] board) {
        String[] originalBoard = { "WBWBWBWB", "BWBWBWBW" };
        int whiteCount = 0;

        for (int i=0;i<8;i++) {
             for (int j=0;j<8;j++) {
                 if (board[row + i].charAt(col + j) != originalBoard[i % 2].charAt(j)) {
                     whiteCount++;
                 }
             }
        }

        // 검은색 시작 체스판을 만들기 위해 다시 칠해야하는 값 == 64 - 흰색 체스판을 만들기 위해 다시 칠해야하는 값
        return Math.min(whiteCount, 64-whiteCount);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] str = br.readLine().split(" ");
        int row = Integer.parseInt(str[0]);
        int col = Integer.parseInt(str[1]);
        
        String[] board = new String[row];
        for (int i=0; i<row; i++) {
            board[i] = br.readLine();
        }

        // 1. 체스판 자르기
        int result = Integer.MAX_VALUE;  // 전체 카운트
        for (int i=0; i<row-7; i++) {
            for (int j=0;j<col-7;j++) {
                // 2. 최소 count 구하기
                int count = getCount(i,j,board);

                // 3. 전체 체스판 count와 비교하기
                if (result > count) {
                    result = count;
                }
            }
        }

        System.out.println(result);
        br.close();
    }
}
