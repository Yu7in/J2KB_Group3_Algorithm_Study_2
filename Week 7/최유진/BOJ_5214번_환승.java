//BOJ_5214번_환승

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static int N, K, M;
	static ArrayList<ArrayList<Integer>> station;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer tokens = new StringTokenizer(br.readLine());

		N = Integer.parseInt(tokens.nextToken());
		K = Integer.parseInt(tokens.nextToken());
		M = Integer.parseInt(tokens.nextToken());

		station = new ArrayList<>();
		for (int i = 0; i <= N + M; i++) {
			station.add(new ArrayList<Integer>());
		}

		for (int i = 1; i <= M; i++) {
			tokens = new StringTokenizer(br.readLine());
			int d = N + i;
			for (int j = 0; j < K; j++) {
				int node = Integer.parseInt(tokens.nextToken());
				station.get(d).add(node);
				station.get(node).add(d);
			}
		}

		int[] checked = new int[101005];
		Queue<Integer> q = new LinkedList<>();
		q.add(1);
		checked[1] = 1;

		while (!q.isEmpty()) {
			int temp = q.poll();

			if (temp == N)
				break;

			for (int x : station.get(temp)) {
				if (checked[x] == 0) {
					q.add(x);
					checked[x] = checked[temp] + 1;
				}
			}
		}

		int ans = checked[N] != 0 ? (checked[N] + 1) / 2 : -1;
		System.out.println(ans);
	}

}
