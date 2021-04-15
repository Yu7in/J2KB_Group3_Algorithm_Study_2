// BOJ_2579번_계단 오르기

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	public static int N;
	public static int[] arr, sum;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		N = Integer.parseInt(br.readLine());
		arr = new int[N + 1];
		arr[0] = 0;
		for (int i = 1; i < N + 1; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}

		sum = new int[N + 1];
		sum[0] = 0;
		sum[1] = arr[1];
		if (N > 1)
			sum[2] = arr[1] + arr[2];
		for (int i = 3; i < N + 1; i++) {
			sum[i] = arr[i] + Math.max(sum[i - 2], sum[i - 3] + arr[i - 1]);
		}

		System.out.println(sum[N]);
	}

}
