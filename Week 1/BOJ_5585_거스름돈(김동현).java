import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        final int[] jpyTypes = {500, 100, 50, 10, 5, 1};
        int qty = 0;

        final Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int charge = 1000 - n;

        for (int coin : jpyTypes) {
           qty += charge / coin;
           charge %= coin;
        }

        System.out.println(qty);
    }
}