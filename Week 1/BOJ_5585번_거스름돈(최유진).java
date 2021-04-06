// BOJ_5585번_거스름돈

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int[] money = { 500, 100, 50, 10, 5, 1 };
		int N = Integer.parseInt(br.readLine());
		
		N = 1000 - N;
		int cnt = 0, idx = 0;
		while (idx < money.length) {
			cnt += (N / money[idx]);
			N %= money[idx];
			idx++;
		}

		System.out.println(cnt);
	}
}