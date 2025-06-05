import javax.swing.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 선언

        String s = br.readLine();
        String[] parts = s.split(" ");

        int a = Integer.parseInt(parts[0]);
        int b = Integer.parseInt(parts[1]);
        int v = Integer.parseInt(parts[2]);

        int res;

        res = (v-b-1)/(a-b)+1;

        System.out.println(res);
    }
}
