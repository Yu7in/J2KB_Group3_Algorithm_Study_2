// BOJ_4963번_섬의 개수

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {

	public static int[][] dirs = { { 0, -1 }, { -1, 0 }, { 0, 1 }, { 1, 0 }, { -1, -1 }, { -1, 1 }, { 1, -1 },
			{ 1, 1 } };

	public static class position {
		int x;
		int y;

		public position(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}

	public static boolean isIn(int row, int col, int h, int w) {
		return row >= 0 && col >= 0 && row < h && col < w;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int w, h;
		Queue<position> q = new LinkedList<>();
		while (true) {
			w = sc.nextInt();
			h = sc.nextInt();
			if (w == 0 && h == 0)
				break;

			int cnt = 0;
			int[][] arr = new int[h][w];
			for (int i = 0; i < arr.length; i++) {
				for (int j = 0; j < arr[i].length; j++) {
					arr[i][j] = sc.nextInt();
				}
			}

			for (int i = 0; i < h; i++) {
				for (int j = 0; j < w; j++) {
					if (arr[i][j] == 1) {
						cnt++;
						q.add(new position(i, j));
						arr[i][j] = 0;
						while (!q.isEmpty()) {
							position po = q.poll();
							for (int k = 0; k < dirs.length; k++) {
								if (isIn(po.x + dirs[k][0], po.y + dirs[k][1], h, w)) {
									if (arr[po.x + dirs[k][0]][po.y + dirs[k][1]] == 1) {
										q.add(new position(po.x + dirs[k][0], po.y + dirs[k][1]));
										arr[po.x + dirs[k][0]][po.y + dirs[k][1]] = 0;
									}
								}
							}
						}
					}
				}
			}
			System.out.println(cnt);
		}
	}

}