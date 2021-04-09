import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        final Scanner scanner = new Scanner(System.in);
        final int n = scanner.nextInt(); // 1. 로프 개수 (1 ≤ N ≤ 100,000)  2. 최대중량 (1 <= N ≤ 10,000)

        int[] weight = new int[n];
        for (int i = 0 ; i < n ; i++) weight[i] = scanner.nextInt();

        Arrays.sort(weight);

        int maxWeight = 0;
        int sum = 0;
        for (int i = 0 ; i < n ; i++){
            sum = weight[i] * (n - i);
            if(maxWeight < sum) maxWeight = sum;
        }

        System.out.println(maxWeight);
    }
}