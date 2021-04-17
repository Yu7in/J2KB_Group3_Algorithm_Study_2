import java.util.Scanner;

/**
 * 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.
 *
 * 1+1+1+1
 * 1+1+2
 * 1+2+1
 * 2+1+1
 * 2+2
 * 1+3
 * 3+1
 * 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
 *
 * 입력
 * 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.
 *
 * 출력
 * 각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.
 *
 * 입력
 * 3 - T
 * 4
 * 7
 * 10
 *
 * 출력
 * 7
 * 44
 * 274
 */
public class Backjoon_9095_123더하기 {

    public static void main(String[] args) {
        final Scanner scanner = new Scanner(System.in);
        final int t = scanner.nextInt();

        int[] dp = new int[11];

        dp[0] = 0;
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;

        //Bottom-Up
        for (int i = 0 ; i < t ; i++){
            int n = scanner.nextInt();
            for (int j = 4; j <= n ; j++) {
                dp[j] = dp[j-1] + dp[j-2] + dp[j-3];
            }
            System.out.println(dp[n]);
        }

    }
}
