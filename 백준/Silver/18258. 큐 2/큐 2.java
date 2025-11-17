import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        Deque<Integer> queue = new ArrayDeque<>();

        StringTokenizer commamd;

        int n = Integer.parseInt(br.readLine());
        for (int i=0;i<n;i++) {
            commamd = new StringTokenizer(br.readLine());

            switch (commamd.nextToken()) {
                case "push":  // 뒤쪽에 데이터 삽입
                    queue.add(Integer.parseInt(commamd.nextToken()));
                    break;
                case "pop" :  // 앞쪽의 데이터 삭제
                    if (queue.size()==0) {
                        sb.append(-1).append('\n');
                    } else {
                        sb.append(queue.getFirst()).append('\n');
                        queue.remove();
                    }
                    break;
                case "size":
                    sb.append(queue.size()).append('\n');
                    break;
                case "empty":
                    if(queue.size()==0) {
                        sb.append(1).append('\n');
                    } else
                        sb.append(0).append('\n');
                    break;
                case "front":
                    if (queue.size()==0) {
                        sb.append(-1).append('\n');
                    } else
                        sb.append(queue.getFirst()).append('\n');
                    break;
                case "back":
                    if (queue.size()==0) {
                        sb.append(-1).append('\n');
                    } else
                        sb.append(queue.getLast()).append('\n');
                    break;
            }
        }
        System.out.println(sb);
    }
}
