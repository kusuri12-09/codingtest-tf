import javax.swing.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int hour = sc.nextInt();
        int minute = sc.nextInt();
        int cook = sc.nextInt();

        minute += cook;

        while (minute >= 60) {
            minute -= 60;
            hour += 1;

            if (hour >= 24) {
                hour -= 24;
            }
        }

        System.out.println(hour +  " " + minute);
    }
}