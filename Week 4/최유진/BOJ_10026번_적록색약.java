// BOJ_10026번_적록색약

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {

	static int ans1, ans2, N;
	static char[][] arr;
	static boolean[][] visited;
	static int[][] dirs = { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } };

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		N = Integer.parseInt(br.readLine());

		arr = new char[N][N];
		for (int i = 0; i < N; i++) {
			arr[i] = br.readLine().toCharArray();
		}

		ans1 = 0;
		visited = new boolean[N][N];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (!visited[i][j]) {
					bfs1(i, j);
				}
			}
		}

		ans2 = 0;
		visited = new boolean[N][N];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (!visited[i][j]) {
					bfs2(i, j);
				}
			}
		}

		System.out.println(ans1 + " " + ans2);
	}

	public static void bfs1(int x, int y) {
		Queue<int[]> q = new LinkedList<>();
		q.add(new int[] { x, y });
		visited[x][y] = true;
		char ch = arr[x][y];

		while (!q.isEmpty()) {
			int[] temp = q.poll();
			for (int i = 0; i < dirs.length; i++) {
				int dx = temp[0] + dirs[i][0];
				int dy = temp[1] + dirs[i][1];
				if (dx >= 0 && dx < N && dy >= 0 && dy < N) {
					if (!visited[dx][dy]) {
						if (arr[dx][dy] == ch) {
							q.add(new int[] { dx, dy });
							visited[dx][dy] = true;
						}
					}
				}
			}
		}

		ans1++;
	}

	public static void bfs2(int x, int y) {
		Queue<int[]> q = new LinkedList<>();
		q.add(new int[] { x, y });
		visited[x][y] = true;
		char ch = arr[x][y];

		while (!q.isEmpty()) {
			int[] temp = q.poll();
			for (int i = 0; i < dirs.length; i++) {
				int dx = temp[0] + dirs[i][0];
				int dy = temp[1] + dirs[i][1];
				if (dx >= 0 && dx < N && dy >= 0 && dy < N) {
					if (!visited[dx][dy]) {
						switch (ch) {
						case 'R':
						case 'G':
							if (arr[dx][dy] == 'R' || arr[dx][dy] == 'G') {
								q.add(new int[] { dx, dy });
								visited[dx][dy] = true;
							}
							break;
						case 'B':
							if (arr[dx][dy] == 'B') {
								q.add(new int[] { dx, dy });
								visited[dx][dy] = true;
							}
							break;
						}
					}
				}
			}
		}

		ans2++;
	}

}
