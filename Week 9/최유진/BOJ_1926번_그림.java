// BOJ_1926번_그림

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	public static int[][] dirs = { { 1, 0 }, { 0, 1 }, { -1, 0 }, { 0, -1 } };

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer tokens = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(tokens.nextToken());
		int m = Integer.parseInt(tokens.nextToken());

		int[][] arr = new int[n][m];
		for (int i = 0; i < n; i++) {
			tokens = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				arr[i][j] = Integer.parseInt(tokens.nextToken());
			}
		}

		int picNum = 0;
		int maxNum = 0;
		boolean[][] visited = new boolean[n][m];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (arr[i][j] == 1 && !visited[i][j]) {
					picNum++;
					int cnt = 0;
					Queue<int[]> q = new LinkedList<int[]>();
					q.add(new int[] { i, j });
					visited[i][j] = true;
					while (!q.isEmpty()) {
						int[] temp = q.poll();
						cnt++;
						for (int k = 0; k < dirs.length; k++) {
							int dx = temp[0] + dirs[k][0];
							int dy = temp[1] + dirs[k][1];
							if (dx >= 0 && dy >= 0 && dx < n && dy < m) {
								if (arr[dx][dy] == 1 && !visited[dx][dy]) {
									q.add(new int[] { dx, dy });
									visited[dx][dy] = true;
								}
							}
						}
					}
					maxNum = maxNum < cnt ? cnt : maxNum;
				}
			}
		}

		System.out.println(picNum);
		System.out.println(maxNum);
	}
}
