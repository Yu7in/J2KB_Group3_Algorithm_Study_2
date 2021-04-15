// BOJ_9095번_1, 2, 3 더하기

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		int[] arr = new int[11];
		arr[1] = 1;
		arr[2] = 2;
		arr[3] = 4;
		for (int i = 4; i < 11; i++) {
			arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3];
		}

		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			int n = Integer.parseInt(br.readLine());
			sb.append(arr[n]).append("\n");
		}

		System.out.println(sb);
	}

}
