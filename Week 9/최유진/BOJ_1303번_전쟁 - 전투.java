// BOJ_1303번_전쟁 - 전투

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

		char[][] arr = new char[M][N];
		for (int i = 0; i < M; i++) {
			String str = br.readLine();
			arr[i] = str.toCharArray();
		}

		int wNum = 0;
		int bNum = 0;
		boolean[][] visited = new boolean[M][N];
		for (int i = 0; i < M; i++) {
			for (int j = 0; j < N; j++) {
				if (!visited[i][j]) {
					int cnt = 0;
					char ch = arr[i][j];
					Queue<int[]> q = new LinkedList<int[]>();
					q.add(new int[] { i, j });
					visited[i][j] = true;
					while (!q.isEmpty()) {
						int[] temp = q.poll();
						cnt++;

						for (int k = 0; k < dirs.length; k++) {
							int dx = temp[0] + dirs[k][0];
							int dy = temp[1] + dirs[k][1];
							if (dx >= 0 && dy >= 0 && dx < M && dy < N) {
								if (!visited[dx][dy] && arr[dx][dy] == ch) {
									q.add(new int[] { dx, dy });
									visited[dx][dy] = true;
								}
							}
						}
					}

					if (ch == 'W') {
						wNum += (cnt * cnt);
					} else {
						bNum += (cnt * cnt);
					}
				}
			}
		}

		System.out.println(wNum + " " + bNum);
	}
}
