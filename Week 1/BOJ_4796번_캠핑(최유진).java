// BOJ_4796번_캠핑

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		int cnt = 0;
		while (true) {
			StringTokenizer tokens = new StringTokenizer(br.readLine());
			int L = Integer.parseInt(tokens.nextToken());
			int P = Integer.parseInt(tokens.nextToken());
			int V = Integer.parseInt(tokens.nextToken());

			if (L == 0 && P == 0 && V == 0)
				break;
			cnt++;

			int n = V / P;
			int n2 = L > V % P ? V % P : L;
			int days = L * n + n2;
			sb.append("Case ").append(cnt).append(": ").append(days).append("\n");
		}
		System.out.println(sb);
	}
}
