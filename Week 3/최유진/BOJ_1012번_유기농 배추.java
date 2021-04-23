// BOJ_1012번_유기농 배추

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	public static int M, N, K;
	public static int[][] arr;
	public static int[][] dirs = { { 1, 0 }, { 0, 1 }, { -1, 0 }, { 0, -1 } };

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		int T = Integer.parseInt(br.readLine());
		for (int tc = 0; tc < T; tc++) {
			StringTokenizer tokens = new StringTokenizer(br.readLine());
			M = Integer.parseInt(tokens.nextToken());
			N = Integer.parseInt(tokens.nextToken());
			K = Integer.parseInt(tokens.nextToken());

			arr = new int[M][N];
			for (int i = 0; i < K; i++) {
				tokens = new StringTokenizer(br.readLine());
				int x = Integer.parseInt(tokens.nextToken());
				int y = Integer.parseInt(tokens.nextToken());
				arr[x][y] = 1;
			}

			int cnt = 0;
			Queue<int[]> q = new LinkedList<>();
			for (int i = 0; i < M; i++) {
				for (int j = 0; j < N; j++) {
					if (arr[i][j] == 1) {
						cnt++;
						q.add(new int[] { i, j });
						arr[i][j] = 0;
						while (!q.isEmpty()) {
							int[] temp = q.poll();
							for (int k = 0; k < dirs.length; k++) {
								int dx = temp[0] + dirs[k][0];
								int dy = temp[1] + dirs[k][1];
								if (dx >= 0 && dy >= 0 && dx < M && dy < N) {
									if (arr[dx][dy] == 1) {
										q.add(new int[] { dx, dy });
										arr[dx][dy] = 0;
									}
								}
							}
						}
					}
				}
			}
			sb.append(cnt).append("\n");
		}
		System.out.println(sb);
	}
}
