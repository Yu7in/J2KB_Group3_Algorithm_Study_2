// BOJ_2178번_미로 탐색

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
		int N = Integer.parseInt(tokens.nextToken());
		int M = Integer.parseInt(tokens.nextToken());

		int[][] arr = new int[N][M];
		for (int i = 0; i < N; i++) {
			String str = br.readLine();
			for (int j = 0; j < str.length(); j++) {
				arr[i][j] = str.charAt(j) - '0';
			}
		}

		boolean[][] visited = new boolean[N][M];
		Queue<int[]> q = new LinkedList<>();
		q.add(new int[] { 0, 0 });
		visited[0][0] = true;
		while (!q.isEmpty()) {
			int[] temp = q.poll();
			for (int i = 0; i < dirs.length; i++) {
				int dx = temp[0] + dirs[i][0];
				int dy = temp[1] + dirs[i][1];
				if (dx >= 0 && dy >= 0 && dx < N && dy < M) {
					if (!visited[dx][dy] && arr[dx][dy] == 1) {
						q.add(new int[] { dx, dy });
						visited[dx][dy] = true;
						arr[dx][dy] = arr[temp[0]][temp[1]] + 1;
					}
				}
			}
		}

		System.out.println(arr[N - 1][M - 1]);
	}
}
